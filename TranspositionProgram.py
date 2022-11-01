import tkinter as tk
from tkinter import ttk
from tkinter import font, RIGHT, LEFT, TOP, END, INSERT
import tkinter.scrolledtext as st
import math

output_choose_list = [
    "Output Window",
    "To File"
]


def click_brute_force(user_message_brute_page, value_to_search, output_choose_combo_box_brute_page,
                      output_brute_page, root):
    """This function do the calculate for : Brute force decrypt /
    Output window / Save to file / Input filter"""
    the_user_message = user_message_brute_page.get("1.0", END)  # Receive The Text
    the_user_message = str(the_user_message).replace("\n", "")  # Replace The \n To Nothing
    if the_user_message == "":
        output_brute_page.delete('1.0', END)
        output_brute_page.insert('1.0', "Please Enter Any Message In The Message Field")
        return

    the_user_value_to_search = value_to_search.get("1.0", END)  # Receive The Key
    the_user_value_to_search = str(the_user_value_to_search).replace("\n", "")  # Replace The \n To Nothing
    if the_user_value_to_search == "":
        output_brute_page.delete('1.0', END)
        output_brute_page.insert('1.0', "Please Type Any Word To Search Inside The Encrypted Message")
        return

    # all the calculate go inside to the_new_string
    the_new_string = ""
    for i in range(2, len(the_user_message)):
        temp_string = decrypt_message(the_user_message, i)

        if the_user_value_to_search in temp_string:
            the_new_string += "The Key = " + str(i) + "-> " + temp_string + "\n"
    if the_new_string == "":
        the_new_string = "No Key Found Match To Your Word Search"


    if output_choose_combo_box_brute_page.get() == "Output Window":
        output_brute_page.delete('1.0', END)
        output_brute_page.insert('1.0', the_new_string)
    elif output_choose_combo_box_brute_page.get() == "To File":
        try:
            file = root.call("tk_getSaveFile", '-initialdir', 'c:\\', '-title', 'Save a file', '-defaultextension',
                             '.txt')
            f = open(file, 'w')
            f.write(the_new_string)
            f.close()

            output_brute_page.delete('1.0', END)
            output_brute_page.insert('1.0', "The Answer Of The Brute Force\nSave Successfully To File !")
        except:
            pass




def open_file_standard_dialog(user_message, root):
    """This function performs the open file standard dialog, taking text
    from file and write it inside the text field"""
    try:
        file = root.call("tk_getOpenFile", '-initialdir', 'c:\\', '-title', 'Open a file')
        f = open(file, 'r')
        user_message.delete('1.0', END)
        user_message.insert(INSERT, f.read())
    except:
        pass




def click_encrypt(user_message, user_value_key, output_choose_combo_box, output, str_choose, root):
    """This function do the calculate for : Encrypt / Decrypt /
    Output window / Save to file / Input filter"""
    the_user_message = user_message.get("1.0", END)  # Receive The Text
    the_user_message = str(the_user_message).replace("\n", "")  # Replace The \n To Nothing
    if the_user_message == "":
        output.delete('1.0', END)
        output.insert('1.0', "Please Enter Any Message In The Message Field")
        return

    the_user_value_key = user_value_key.get("1.0", END)  # Receive The Key
    the_user_value_key = str(the_user_value_key).replace("\n", "")  # Replace The \n To Nothing
    if not the_user_value_key.isnumeric():
        output.delete('1.0', END)
        output.insert('1.0', "Please Enter Only Int Number In Key Field")
        return

    the_user_value_key = int(the_user_value_key)

    if the_user_value_key < 2 or the_user_value_key >= len(the_user_message):
        output.delete('1.0', END)
        output.insert('1.0', "Please Enter Int Number In Key Field\nSmaller Than The Length Of Your Message,"
                             "\nand Bigger From 1")
        return

    the_new_string = ""
    if str_choose.get() == 'null':
        output.delete('1.0', END)
        output.insert('1.0', "Please Choose Encrypt / Decrypt")
        return
    elif str_choose.get() == "Encrypt":
        the_new_string = encrypt_message(the_user_message, the_user_value_key)
    elif str_choose.get() == "Decrypt":
        the_new_string = decrypt_message(the_user_message, the_user_value_key)


    if output_choose_combo_box.get() == "Output Window":
        output.delete('1.0', END)
        output.insert('1.0', the_new_string)
    elif output_choose_combo_box.get() == "To File":
        try:
            file = root.call("tk_getSaveFile", '-initialdir', 'c:\\', '-title', 'Save a file', '-defaultextension',
                             '.txt')
            f = open(file, 'w')
            f.write(the_new_string)
            f.close()

            output.delete('1.0', END)
            if str_choose.get() == "Encrypt":
                output.insert('1.0', "The Encrypted Message Save Successfully To File !")
            elif str_choose.get() == "Decrypt":
                output.insert('1.0', "The Decrypted Message Save Successfully To File !")
        except:
            pass


def decrypt_message(message, key):
    """This function performs the decryption of the "encrypted message"
    received from the user"""
    num_of_columns = math.ceil(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)
    plaintext = [''] * num_of_columns
    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)


def encrypt_message(message, key):
    """This function performs the encryption of the message received from the user"""
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)



def go_brute_force_page(note):
    """This function performs the brute force button in home page"""
    note.select(2)


def go_regular_page(note):
    """This function performs the regular encrypt / decrypt button in home page"""
    note.select(1)


def go_back(note):
    """This function performs the back button"""
    note.select(0)


def two_options(root, back_button, str_choose):
    """This function includes all data inside root: Frames, Notebook, Fields, Buttons"""
    text_font = font.Font(family="Calibri", size=15, weight=font.BOLD)
    menu_font = font.Font(family="Helvetica", size=11, weight=font.BOLD)
    style = ttk.Style()
    style.layout('TNotebook.Tab', [])
    note = ttk.Notebook(root)

    page1 = ttk.Frame(note)

    choose_text_label = tk.Label(page1, text="\nWelcome!\n\nPlease Choose Your Option :\n\n", width=100,
                                 font=text_font)
    choose_text_label.pack()
    btn_regular = tk.Button(page1, text='Regular Encrypt / Decrypt',  width=50, bg='#CCFF00',
                            activebackground='#8ABC2F', bd=4, activeforeground="black", relief="raised",
                            font=menu_font, command=lambda: go_regular_page(note))
    btn_regular.pack()
    lines_label = tk.Label(page1)  # Create Space Between The Buttons
    lines_label.pack()
    btn_brute_force = tk.Button(page1, text='Brute Force',  width=50, bg='#04adff', activebackground='#72AEC3',
                                bd=4, activeforeground="black", relief="raised", font=menu_font,
                                command=lambda: go_brute_force_page(note))
    btn_brute_force.pack()
    lines_label2 = tk.Label(page1)  # Create Space Between The Buttons
    lines_label2.pack()
    btn_exit = tk.Button(page1, text='Exit',  width=50, bg='#b1c8e0', activebackground='#3b7e7e', bd=4,
                         activeforeground="black", relief="raised", font=menu_font, command=lambda: exit())
    btn_exit.pack()

    # background_label = tk.Label(page1, image=background_image)
    # background_label.place(x=-100, y=130, width=370)

    note.add(page1)

    page2 = ttk.Frame(note)
    btn_back = tk.Button(page2, border=0, image=back_button, command=lambda: go_back(note))
    btn_back.pack()

    first_labelframe = tk.LabelFrame(page2, font=text_font, height=3, border=0)
    first_labelframe.pack()

    user_message = st.ScrolledText(first_labelframe, font=text_font, bg='white', width=55, height=3)
    user_message.pack(side=LEFT)
    user_message.insert('1.0', 'Enter Your Message Here')

    or_label = tk.Label(first_labelframe, text=" Or -> ", font=text_font)
    or_label.pack(side=LEFT)

    open_from_file_button = tk.Button(first_labelframe, text="Click Here To Upload \nInput From File",
                                      font=text_font, bg="#fa9954", fg="#fff",
                                      command=lambda: open_file_standard_dialog(user_message, root))
    open_from_file_button.pack(side=RIGHT)

    lines_label3 = tk.Label(page2)  # Create Space Between The Text Fields
    lines_label3.pack()

    user_value_key = st.ScrolledText(page2, font=text_font, bg='white', width=43, height=3)
    user_value_key.pack()
    user_value_key.insert('1.0', 'Enter Here Your Key ( Only Numbers )')

    second_labelframe = tk.LabelFrame(page2, font=text_font, height=3, border=0)
    second_labelframe.pack()

    output_choose_labelframe = tk.LabelFrame(second_labelframe, font=text_font, height=3, border=0)
    output_choose_labelframe.pack(side=RIGHT)

    choose_text_label2 = tk.Label(output_choose_labelframe, text="Choose Where To \nOutput From List :\n",
                                  height=3, width=30, font=text_font)
    choose_text_label2.pack(side=TOP)

    output_choose_combo_box = ttk.Combobox(output_choose_labelframe, value=output_choose_list, font=menu_font)
    output_choose_combo_box.current(0)

    output_choose_combo_box.bind("<<ComboboxSelected>>",
                                 lambda e=None: click_encrypt(user_message, user_value_key,
                                                              output_choose_combo_box, output, str_choose, root))
    output_choose_combo_box.pack()

    choose_option_labelframe = tk.LabelFrame(second_labelframe, font=text_font, height=3, border=0)
    choose_option_labelframe.pack(side=LEFT)

    choose_text_label3 = tk.Label(choose_option_labelframe, text="Choose Your Action :", height=2, width=30,
                                  font=text_font)
    choose_text_label3.pack(side=TOP)
    str_choose.set('null')
    first_button = tk.Radiobutton(choose_option_labelframe, text="Encrypt", value='Encrypt', variable=str_choose,
                                  font=text_font,
                                  command=lambda e=None: click_encrypt(user_message, user_value_key,
                                                                       output_choose_combo_box, output,
                                                                       str_choose, root))
    first_button.pack(side=TOP)
    second_button = tk.Radiobutton(choose_option_labelframe, text="Decrypt", value='Decrypt', variable=str_choose,
                                   font=text_font,
                                   command=lambda e=None: click_encrypt(user_message, user_value_key,
                                                                        output_choose_combo_box, output,
                                                                        str_choose, root))
    second_button.pack(side=TOP)

    text_label_output = tk.Label(page2, text="This Is Your Output :", height=2, font=text_font)
    text_label_output.pack()
    output = st.ScrolledText(page2, height=100, bg="#8ABC2F", width=65, font=text_font)
    output.pack(pady=15)

    note.add(page2)

    page3 = ttk.Frame(note)
    btn_back_brute_page = tk.Button(page3, border=0, image=back_button, command=lambda: go_back(note))
    btn_back_brute_page.pack()

    first_labelframe_brute_page = tk.LabelFrame(page3, font=text_font, height=3, border=0)
    first_labelframe_brute_page.pack()

    user_message_brute_page = st.ScrolledText(first_labelframe_brute_page, font=text_font, bg='white',
                                              width=55, height=3)
    user_message_brute_page.pack(side=LEFT)
    user_message_brute_page.insert('1.0', 'Enter Your Encrypted Message Here')

    or_label_brute_page = tk.Label(first_labelframe_brute_page, text=" Or -> ", font=text_font)
    or_label_brute_page.pack(side=LEFT)

    open_from_file_button_brute_page = tk.Button(first_labelframe_brute_page,
                                                 text="Click Here To Upload \nInput From File", font=text_font,
                                                 bg="#fa9954", fg="#fff",
                                                 command=lambda: open_file_standard_dialog(user_message_brute_page,
                                                                                           root))
    open_from_file_button_brute_page.pack(side=RIGHT)

    lines_label4 = tk.Label(page3)  # Create Space Between The Text Fields
    lines_label4.pack()

    value_to_search = st.ScrolledText(page3, font=text_font, bg='white', width=43, height=3)
    value_to_search.pack()
    value_to_search.insert('1.0', 'Type The Word Or Sentence\nYou Want To Search In The\nEncrypted Message')

    lines_label5 = tk.Label(page3)  # Create Space Between The Text Fields
    lines_label5.pack()

    second_labelframe_brute_page = tk.LabelFrame(page3, font=text_font, height=3, border=0)
    second_labelframe_brute_page.pack()

    output_choose_labelframe_brute_page = tk.LabelFrame(second_labelframe_brute_page, font=text_font,
                                                        height=3, border=0)
    output_choose_labelframe_brute_page.pack(side=RIGHT)

    choose_text_label4 = tk.Label(output_choose_labelframe_brute_page,
                                  text="Choose Where To \nOutput From List :\n", height=3, width=30,
                                  font=text_font)
    choose_text_label4.pack(side=TOP)

    output_choose_combo_box_brute_page = ttk.Combobox(output_choose_labelframe_brute_page,
                                                      value=output_choose_list, font=menu_font)
    output_choose_combo_box_brute_page.current(0)

    output_choose_combo_box_brute_page.bind("<<ComboboxSelected>>",
                                lambda e=None: click_brute_force(user_message_brute_page, value_to_search,
                                                                 output_choose_combo_box_brute_page,
                                                                 output_brute_page, root))
    output_choose_combo_box_brute_page.pack()

    button_brute_force_labelframe = tk.LabelFrame(second_labelframe_brute_page, font=text_font, height=3, border=0)
    button_brute_force_labelframe.pack(side=LEFT)

    press_button_brute_force = tk.Button(button_brute_force_labelframe, text="Click Here To\nBrute Force",
                                         font="Halvetica 22", bg="#2c9fdb", fg="#fff", width=16,
                                         command=lambda e=None:
                                         click_brute_force(user_message_brute_page, value_to_search,
                                                           output_choose_combo_box_brute_page, output_brute_page,
                                                           root))
    press_button_brute_force.pack(side=RIGHT)

    text_label_output2 = tk.Label(page3, text="This Is Your Output :", height=2, font=text_font)
    text_label_output2.pack()
    output_brute_page = st.ScrolledText(page3, height=100, bg="#2c9fdb", width=65, font=text_font)
    output_brute_page.pack(pady=15)

    note.add(page3)

    note.pack(expand=1, fill='both', padx=5, pady=5)


def main():
    """This is main function"""
    root = tk.Tk()  # יצירת הרוט
    root.geometry("1000x600+130+30")   # גודל החלון ומיקום
    root.resizable(width=tk.FALSE, height=tk.FALSE)
    root.title("Tomer Aminov - Project")   # כותרת החלון
    str_choose = tk.StringVar()
    # background_image = tk.PhotoImage(file="encryption_logo.png")
    back_button = tk.PhotoImage(file="back_button.png")
    two_options(root, back_button, str_choose)
    tk.mainloop()


if __name__ == "__main__":
    main()
