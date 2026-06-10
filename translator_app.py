import customtkinter as ctk
from deep_translator import GoogleTranslator

# ------------------ Languages ------------------

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Marathi": "mr",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar"
}

# ------------------ Functions ------------------

def translate_text():
    text = input_text.get("1.0", "end").strip()

    if not text:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", "Please enter some text.")
        return

    source_lang = languages[source_var.get()]
    target_lang = languages[target_var.get()]

    try:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        output_text.delete("1.0", "end")
        output_text.insert("1.0", translated)

    except Exception as e:
        output_text.delete("1.0", "end")
        output_text.insert("1.0", f"Error: {e}")


def copy_text():
    translated = output_text.get("1.0", "end").strip()

    app.clipboard_clear()
    app.clipboard_append(translated)


def swap_languages():
    source = source_var.get()
    target = target_var.get()

    source_var.set(target)
    target_var.set(source)

# ------------------ App ------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
text="AI Powered Language Translation Tool"
app.geometry("900x650")

# Title
title = ctk.CTkLabel(
    app,
    text="AI Powered Language Translation Tool",
    font=("Arial", 26, "bold")
)
title.pack(pady=20)

# Input Label
input_label = ctk.CTkLabel(
    app,
    text="Enter Text"
)
input_label.pack()

# Input Box
input_text = ctk.CTkTextbox(
    app,
    width=700,
    height=140
)
input_text.pack(pady=10)

# Language Selection Frame
language_frame = ctk.CTkFrame(app)
language_frame.pack(pady=10)

source_var = ctk.StringVar(value="English")
target_var = ctk.StringVar(value="Hindi")

source_menu = ctk.CTkOptionMenu(
    language_frame,
    values=list(languages.keys()),
    variable=source_var
)
source_menu.pack(side="left", padx=20, pady=10)

target_menu = ctk.CTkOptionMenu(
    language_frame,
    values=list(languages.keys()),
    variable=target_var
)
target_menu.pack(side="left", padx=20, pady=10)

# Buttons Frame
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=15)

translate_btn = ctk.CTkButton(
    button_frame,
    text="Translate",
    command=translate_text,
    width=150
)
translate_btn.pack(side="left", padx=10)

swap_btn = ctk.CTkButton(
    button_frame,
    text="Swap",
    command=swap_languages,
    width=120
)
swap_btn.pack(side="left", padx=10)

copy_btn = ctk.CTkButton(
    button_frame,
    text="Copy",
    command=copy_text,
    width=120
)
copy_btn.pack(side="left", padx=10)

# Output Label
output_label = ctk.CTkLabel(
    app,
    text="Translated Text"
)
output_label.pack()

# Output Box
output_text = ctk.CTkTextbox(
    app,
    width=700,
    height=140
)
output_text.pack(pady=10)

app.mainloop()