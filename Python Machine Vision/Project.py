import mediapipe as mp
import cv2
import numpy as np
import random
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

shapes = ['circle', 'square', 'triangle', 'hexagon']

colors = {'circle': (0, 0, 255),  # Blue
          'square': (0, 255, 0),  # Green
          'triangle': (255, 0, 0),  # Red
          'hexagon': (28, 172, 255)}  # orange

score = 0
x_enemy = {shape: random.randint(50, 600) for shape in shapes}
y_enemy = {shape: random.randint(50, 400) for shape in shapes}
visible_shapes = ['triangle', 'hexagon']

def draw_circle(image, center, radius, color):
    cv2.circle(image, center, radius, color, 5)

def draw_square(image, top_left, side_length, color):
    bottom_right = (top_left[0] + side_length, top_left[1] + side_length)
    cv2.rectangle(image, top_left, bottom_right, color, 5)

def draw_triangle(image, vertices, color):
    pts = np.array(vertices, np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], isClosed=True, color=color, thickness=5)

def draw_hexagon(image, center, side_length, color):
    hexagon_pts = []
    for i in range(6):
        x = int(center[0] + side_length * np.cos(i * 2 * np.pi / 6))
        y = int(center[1] + side_length * np.sin(i * 2 * np.pi / 6))
        hexagon_pts.append((x, y))
    cv2.polylines(image, [np.array(hexagon_pts)], isClosed=True, color=color, thickness=5)

def draw_enemies(image):
    for shape, x, y in zip(shapes, x_enemy.values(), y_enemy.values()):
        if shape == 'circle':
            draw_circle(image, (x, y), 25, colors[shape])
        elif shape == 'square':
            draw_square(image, (x - 25, y - 25), 50, colors[shape])
        elif shape == 'triangle':
            draw_triangle(image, [(x, y - 25), (x - 25, y + 25), (x + 25, y + 25)], colors[shape])
        elif shape == 'hexagon':
            draw_hexagon(image, (x, y), 30, colors[shape])

video = cv2.VideoCapture(0)

# Set the game duration in seconds
game_duration = 60
start_time = time.time()

shapes_update_interval = 5  # Update shapes every 5 seconds
last_shapes_update_time = time.time()

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape

        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, game_duration - elapsed_time)

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 255)
        text = cv2.putText(image, "Score", (480, 30), font, 1, color, 4, cv2.LINE_AA)
        text = cv2.putText(image, str(score), (590, 30), font, 1, color, 4, cv2.LINE_AA)

        if remaining_time <= 0:
            text = cv2.putText(image, "TIME'S UP!", (200, 200), font, 2, (0, 0, 255), 4, cv2.LINE_AA)

        if time.time() - last_shapes_update_time >= shapes_update_interval:
            last_shapes_update_time = time.time()
            for shape in visible_shapes:
                x_enemy[shape] = random.randint(50, 600)
                y_enemy[shape] = random.randint(50, 400)

        draw_enemies(image)

        # Display timer
        timer_text = f"Time: {remaining_time // 60:02}:{remaining_time % 60:02}"
        text = cv2.putText(image, timer_text, (30, 30), font, 1, color, 4, cv2.LINE_AA)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))

                if num == 0:  # Left hand (square)
                    for point in mp_hands.HandLandmark:
                        normalized_landmark = hand.landmark[point]
                        pixel_coordinates_landmark = mp_drawing._normalized_to_pixel_coordinates(
                            normalized_landmark.x, normalized_landmark.y, imageWidth, imageHeight)
                        point = str(point)

                        if point == 'HandLandmark.INDEX_FINGER_TIP':
                            try:
                                draw_square(image, (pixel_coordinates_landmark[0] - 25, pixel_coordinates_landmark[1] - 25), 50, colors['square'])
                                if x_enemy['square'] - 10 <= pixel_coordinates_landmark[0] <= x_enemy['square'] + 10:
                                    print("Square found")
                                    x_enemy['square'] = random.randint(50, 600)
                                    y_enemy['square'] = random.randint(50, 400)
                                    score += 1
                            except:
                                pass

                elif num == 1:  # Right hand (circle)
                    for point in mp_hands.HandLandmark:
                        normalized_landmark = hand.landmark[point]
                        pixel_coordinates_landmark = mp_drawing._normalized_to_pixel_coordinates(
                            normalized_landmark.x, normalized_landmark.y, imageWidth, imageHeight)
                        point = str(point)

                        if point == 'HandLandmark.INDEX_FINGER_TIP':
                            try:
                                draw_circle(image, (pixel_coordinates_landmark[0], pixel_coordinates_landmark[1]), 25, colors['circle'])
                                if x_enemy['circle'] - 10 <= pixel_coordinates_landmark[0] <= x_enemy['circle'] + 10:
                                    print("Circle found")
                                    x_enemy['circle'] = random.randint(50, 600)
                                    y_enemy['circle'] = random.randint(50, 400)
                                    score += 1
                            except:
                                pass

        cv2.imshow('Hand Tracking', image)

        if remaining_time == 0:
            print("TIME'S UP!")
            print("Final Score:", score)
            cv2.waitKey(0)  # Wait until any key is pressed
            break

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("Final Score:", score)
            break

video.release()
cv2.destroyAllWindows()