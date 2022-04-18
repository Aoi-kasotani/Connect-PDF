import PyPDF2
import datetime
import tkinter
import tkinter.filedialog

global pdf1
global pdf2
global pdf3
global pdf4
pdf1 = ""
pdf2 = ""
pdf3 = ""
pdf4 = ""

def file_read():
  # ファイル選択ダイアログの表示
  file_path = tkinter.filedialog.askopenfilename(filetypes=[("PDFファイル", "*.pdf")],title="結合したいPDF",multiple="False")

  # ファイルが選択された場合、ファイル名を返す
  if len(file_path) != 0:
    pdf_path = file_path
  # ファイル選択がキャンセルされた場合は空白にする
  else:
    pdf_path = ""

  return pdf_path

class Application(tkinter.Tk):
  def __init__(self):
    super().__init__()

    # アプリのタイトル、サイズ（変更不可）、背景色
    self.title("PDF結合")
    self.geometry("600x300")
    self.resizable(width=False, height=False)
    self.configure(bg="light steel blue")

    # 選択されたPDFファイル名を表示する領域
    self.path1 = tkinter.Entry(width=70) 
    self.path1.insert(tkinter.END, "1つ目")
    self.path1.configure(state="readonly")
    self.path1.place(x=20, y=25)

    self.path2 = tkinter.Entry(width=70)
    self.path2.insert(tkinter.END, "2つ目")
    self.path2.configure(state="readonly")
    self.path2.place(x=20, y=75)

    self.path3 = tkinter.Entry(width=70) 
    self.path3.insert(tkinter.END, "3つ目")
    self.path3.configure(state="readonly")
    self.path3.place(x=20, y=125)

    self.path4 = tkinter.Entry(width=70) 
    self.path4.insert(tkinter.END, "4つ目")
    self.path4.configure(state="readonly")
    self.path4.place(x=20, y=175)

    # 1~4：読み込みボタンの作成と配置
    self.read_button1 = tkinter.Button(self,text="ファイル読み込み",command=self.read_button_func1,bg="lemon chiffon")
    self.read_button1.place(x=490, y=22)

    self.read_button2 = tkinter.Button(self,text="ファイル読み込み",command=self.read_button_func2,bg="lemon chiffon")
    self.read_button2.place(x=490, y=72)
 
    self.read_button3 = tkinter.Button(self,text="ファイル読み込み",command=self.read_button_func3,bg="lemon chiffon")
    self.read_button3.place(x=490, y=122)

    self.read_button4 = tkinter.Button(self,text="ファイル読み込み",command=self.read_button_func4,bg="lemon chiffon")
    self.read_button4.place(x=490, y=172)

    # 結合実行ボタンの作成と配置
    self.read_button5 = tkinter.Button(self,text="結合",command=self.read_button_func5,width=30,height=2,font=("bold",20))
    self.read_button5.place(x=85, y=213)

    # 6~9：選択削除ボタンの作成と配置
    self.read_button6 = tkinter.Button(self,text="×",command=self.read_button_func6,bg="light salmon")
    self.read_button6.place(x=460, y=22)

    self.read_button7 = tkinter.Button(self,text="×",command=self.read_button_func7,bg="light salmon")
    self.read_button7.place(x=460, y=72)
 
    self.read_button8 = tkinter.Button(self,text="×",command=self.read_button_func8,bg="light salmon")
    self.read_button8.place(x=460, y=122)

    self.read_button9 = tkinter.Button(self,text="×",command=self.read_button_func9,bg="light salmon")
    self.read_button9.place(x=460, y=172)

  def read_button_func1(self):
    global pdf1
    # ファイルを読み込み
    pdf1 = file_read()
    # 選択されたPDFファイル名を領域に表示
    self.path1.configure(state="normal")
    self.path1.delete(0, tkinter.END)
    if pdf1 != "":
      self.path1.insert(tkinter.END, pdf1)
    else:
      self.path1.insert(tkinter.END, "1つ目")
    self.path1.configure(state="readonly")
 
  def read_button_func2(self):
    global pdf2
    pdf2 = file_read()
    self.path2.configure(state="normal")
    self.path2.delete(0, tkinter.END)
    if pdf2 != "":
      self.path2.insert(tkinter.END, pdf2)
    else:
      self.path2.insert(tkinter.END, "2つ目")
    self.path2.configure(state="readonly")
 
  def read_button_func3(self):
    global pdf3
    pdf3 = file_read()
    self.path3.configure(state="normal")
    self.path3.delete(0, tkinter.END)
    if pdf3 != "":
      self.path3.insert(tkinter.END, pdf3)
    else:
      self.path3.insert(tkinter.END, "3つ目")
    self.path3.configure(state="readonly")

  def read_button_func4(self):
    global pdf4
    pdf4 = file_read()
    self.path4.configure(state="normal")
    self.path4.delete(0, tkinter.END)
    if pdf4 != "":
      self.path4.insert(tkinter.END, pdf4)
    else:
      self.path4.insert(tkinter.END, "4つ目")
    self.path4.configure(state="readonly")

  def read_button_func5(self):
    global pdf1
    global pdf2
    global pdf3
    global pdf4
    pdf_files = []

    # 選択されたPDFファイルをリストに入れる
    if pdf1 != "":
      pdf_files.append(pdf1)
    if pdf2 != "":
      pdf_files.append(pdf2)
    if pdf3 != "":
      pdf_files.append(pdf3)
    if pdf4 != "":
      pdf_files.append(pdf4)

    if pdf_files != []:
      # PDFファイルを結合
      pdf_writer = PyPDF2.PdfFileWriter()
      for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for i in range(pdf_reader.getNumPages()):
          pdf_writer.addPage(pdf_reader.getPage(i))

      # 名前を付けて保存ウィンドウを表示
      merged_file = tkinter.filedialog.asksaveasfilename(filetypes=[("PDFファイル", ".pdf")],defaultextension="pdf")
      # 保存
      with open(merged_file, "wb") as f:
        pdf_writer.write(f)

    else:
      return

  def read_button_func6(self):
    global pdf1
    # PDF選択をなかったことにする
    pdf1 = ""
    # 表示されていたPDFファイル名を削除
    self.path1.configure(state="normal")
    self.path1.delete(0, tkinter.END)
    self.path1.insert(tkinter.END, "1つ目")
    self.path1.configure(state="readonly")

  def read_button_func7(self):
    global pdf2
    pdf2 = ""
    self.path2.configure(state="normal")
    self.path2.delete(0, tkinter.END)
    self.path2.insert(tkinter.END, "2つ目")
    self.path2.configure(state="readonly")

  def read_button_func8(self):
    global pdf3
    pdf3 = ""
    self.path3.configure(state="normal")
    self.path3.delete(0, tkinter.END)
    self.path3.insert(tkinter.END, "3つ目")
    self.path3.configure(state="readonly")

  def read_button_func9(self):
    global pdf4
    pdf4 = ""
    self.path4.configure(state="normal")
    self.path4.delete(0, tkinter.END)
    self.path4.insert(tkinter.END, "4つ目")
    self.path4.configure(state="readonly")

# GUIアプリ生成
app = Application()
app.mainloop()
