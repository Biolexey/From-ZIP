from tkinter import Tk, Canvas
import sys

W, H = (400, 300)

def display(canvas, msg):
	canvas.create_line((0, 0), (W-1, H-1))
	canvas.create_line((0, H-1), (W-1, 0))
	canvas.create_text((W/2, H/2), text=msg)

def main():
	if(len(sys.argv) > 1):
		msg = sys.argv[1]

	else:
		msg = input("message -> ")
	
	root = Tk()
	canvas = Canvas(root, width=W, height=H, highlightthickness=0)
	canvas.pack()		#canvasの配置確定

	display(canvas, msg)
	root.mainloop()		#ルートフレームの実行ループ開始

if(__name__ == "__main__"):
	main()