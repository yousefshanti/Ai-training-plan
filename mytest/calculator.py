import tkinter as tk


BG_COLOR      = "#F0F2F5"   # خلفية النافذة (رمادي فاتح)
DISPLAY_BG    = "#FFFFFF"   # خلفية الشاشة
TEXT_COLOR    = "#1A1A2E"   # لون النص الأساسي
NUM_BG        = "#FFFFFF"   # خلفية أزرار الأرقام
NUM_HOVER     = "#E4E7EB"   # لون أزرار الأرقام عند مرور الماوس
OP_BG         = "#FF8C42"   # خلفية أزرار العمليات (برتقالي)
OP_HOVER      = "#FF7020"   # لون العمليات عند مرور الماوس
EQ_BG         = "#4A6CF7"   # خلفية زر يساوي (أزرق)
EQ_HOVER      = "#3A56D4"   # لون يساوي عند مرور الماوس
CLEAR_BG      = "#EF5350"   # خلفية زر المسح (أحمر)
CLEAR_HOVER   = "#E53935"   # لون المسح عند مرور الماوس

FONT          = ("Segoe UI", 20)
DISPLAY_FONT  = ("Segoe UI", 40, "bold")
SMALL_FONT    = ("Segoe UI", 16)


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x520")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.expression = ""          # النص الحالي للعملية

        self._build_display()
        self._build_buttons()

    # ---------- الشاشة ----------
    def _build_display(self):
        display_frame = tk.Frame(self.root, bg=BG_COLOR)
        display_frame.pack(fill="both", padx=20, pady=(30, 10))

        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=DISPLAY_FONT,
            bg=DISPLAY_BG,
            fg=TEXT_COLOR,
            anchor="e",          # محاذاة النص لليمين
            padx=20,
            pady=30,
        )
        self.display.pack(fill="both")

    # ---------- الأزرار ----------
    def _build_buttons(self):
        btn_frame = tk.Frame(self.root, bg=BG_COLOR)
        btn_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # تخطيط الأزرار: (النص، الصف، العمود، النوع، عدد الأعمدة)
        buttons = [
            ("C", 0, 0, "clear", 1), ("⌫", 0, 1, "clear", 1),
            ("÷", 0, 2, "op", 1),    ("×", 0, 3, "op", 1),

            ("7", 1, 0, "num", 1), ("8", 1, 1, "num", 1),
            ("9", 1, 2, "num", 1), ("−", 1, 3, "op", 1),

            ("4", 2, 0, "num", 1), ("5", 2, 1, "num", 1),
            ("6", 2, 2, "num", 1), ("+", 2, 3, "op", 1),

            ("1", 3, 0, "num", 1), ("2", 3, 1, "num", 1),
            ("3", 3, 2, "num", 1), ("=", 3, 3, "eq", 2),

            ("0", 4, 0, "num", 2), (".", 4, 2, "num", 1),
        ]

        # اجعل كل الصفوف والأعمدة تتمدّد بالتساوي
        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        for (text, row, col, kind, colspan) in buttons:
            self._create_button(btn_frame, text, row, col, kind, colspan)

    def _create_button(self, parent, text, row, col, kind, colspan):
        # اختيار الألوان حسب نوع الزر
        if kind == "num":
            bg, hover, fg = NUM_BG, NUM_HOVER, TEXT_COLOR
        elif kind == "op":
            bg, hover, fg = OP_BG, OP_HOVER, "#FFFFFF"
        elif kind == "eq":
            bg, hover, fg = EQ_BG, EQ_HOVER, "#FFFFFF"
        else:  # clear
            bg, hover, fg = CLEAR_BG, CLEAR_HOVER, "#FFFFFF"

        btn = tk.Button(
            parent,
            text=text,
            font=FONT,
            bg=bg,
            fg=fg,
            activebackground=hover,
            activeforeground=fg,
            relief="flat",           # يشيل الحدود القديمة
            bd=0,
            cursor="hand2",          # شكل اليد عند المرور
            command=lambda t=text: self.on_click(t),
        )
        btn.grid(
            row=row, column=col, columnspan=colspan,
            sticky="nsew", padx=5, pady=5,
        )

        # تأثير hover: تغيير اللون عند دخول/خروج الماوس
        btn.bind("<Enter>", lambda e, b=btn, h=hover: b.config(bg=h))
        btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))

    # ---------- المنطق ----------
    def on_click(self, char):
        if char == "C":
            self.expression = ""
            self.display_var.set("0")

        elif char == "⌫":
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression if self.expression else "0")

        elif char == "=":
            self.calculate()

        else:
            # تحويل الرموز الجميلة لرموز بايثون
            symbols = {"÷": "/", "×": "*", "−": "-"}
            if char in symbols:
                self.expression += symbols[char]
            else:
                self.expression += char
            self.display_var.set(self.expression)

    def calculate(self):
        try:
            # eval يحسب العملية الحسابية من النص
            result = eval(self.expression)
            # لو النتيجة رقم صحيح، اعرضه بدون .0
            if result == int(result):
                result = int(result)
            self.display_var.set(str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            self.display_var.set("Error: ÷0")
            self.expression = ""
        except Exception:
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
