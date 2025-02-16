from datetime import datetime 
import os
from terminalColors import bcolors
from ultralytics import YOLO
import time
import cv2

now = datetime.now()

class ChocolateDefender:
    def __init__(self, startTime, endTime,):
        self.detectionModel = YOLO("yolov8m.pt")
        self.now = datetime.now()
        self.hunt = False
        self.detectedPerson = False

        #check and see if the start and stop time can succesfully be converted
        try:
            print(f"Start Input: {startTime} End Time: {endTime}")
            self.start = datetime.strptime(startTime, '%d/%m/%y %H:%M:%S')
            self.end = datetime.strptime(endTime, '%d/%m/%y %H:%M:%S')
        except:
            print(f"{bcolors.FAIL} Input time format incorrect, please put in a time like such: '19:00:00' ")
            exit()

    def timecheck(self, currentTime):
        if currentTime >= self.start and currentTime <= self.end:
            print(f"{bcolors.WARNING} THE HUNT IS ON...")
            self.hunt = True
            return self.hunt
        else:
            print(f"{bcolors.OKGREEN} Rose can eat!")
            self.hunt = False
            return self.hunt

    def parentWarn(self):
        pass

    def main(self):
        print(f"{bcolors.OKBLUE} Welcome to the Pantry Defender... Defeat Rose in her quest for morning snacks... Current Time: {self.now}")

        self.now = datetime.now()
        self.timecheck(self.now)
        if self.hunt:
            #activate camera
            self.cap=cv2.VideoCapture(0)
            #Give parents a minute to go upstairs...
            time.sleep(30)
            #Alert parents of system activation
            os.system("ffplay -nodisp -autoexit -af volume=6.0 Activated.mp4")

            while self.hunt:
                self.now = datetime.now()
                self.timecheck(self.now)
                print(f"{bcolors.OKGREEN} Hunting... Current Time {self.now} Window: {self.start} - {self.end}")
                
                ret, frame = self.cap.read()
                
                if not ret:
                    print("Error: Failed to capture image.")
                    break

                results = self.detectionModel(frame)

                self.detectedPerson = False
                for result in results:
                    annotated_frame = result.plot()
                    for box in result.boxes:
                        cls = int(box.cls[0])
                        if cls == 0:
                            self.detectedPerson = True
                            os.system("ffplay -nodisp -autoexit -af volume=6.0 Rose_Message.mp4")


                cv2.imshow("Rose Smelling...", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            self.cap.release()
            cv2.destroyAllWindows()
        else:
            self.timecheck(self.now)


if __name__ == '__main__':
    defense = ChocolateDefender('16/02/25 12:30:00', '17/02/25 07:30:00')
    defense.main()
