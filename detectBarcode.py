import cv2
import pyzbar.pyzbar as pyzbar

code = ''

# 바코드 인식 및 테두리 설정
def read_frame(frame):
    global code
    
    try:    
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, barcode_info, (x , y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            code = barcode_info

        return frame
    except Exception as e: print(e)

def main():
    try:
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                frame = read_frame(frame)
                cv2.imshow("barcode reader", frame)
                print(code)
                if cv2.waitKey(25) == 27: break
            else:
                print("예외")
                break

    except Exception as e: print(e)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__': main()