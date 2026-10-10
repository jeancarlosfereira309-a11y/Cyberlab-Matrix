#
import random
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

VERDE = (0.2, 1, 0.35, 1)
PRETO = (0.015, 0.02, 0.015, 1)

class MatrixApp(App):
    def build(self):
        Window.clearcolor = PRETO
        self.rodando = True
        self.raindrops = []
        self.rootbox = FloatLayout()

        self.titulo = Label(
            text="[b]CYBERLAB // MATRIX[/b]",
            markup=True, color=VERDE,
            font_size="25sp", size_hint=(1, .12),
            pos_hint={"x": 0, "top": 1}
        )
        self.rootbox.add_widget(self.titulo)

        self.status = Label(
            text="SYSTEM ONLINE",
            color=VERDE, font_size="14sp",
            size_hint=(1, .08),
            pos_hint={"x": 0, "y": .03}
        )
        self.rootbox.add_widget(self.status)

        self.botao = Button(
            text="PAUSAR MATRIX",
            size_hint=(.7, .09),
            pos_hint={"center_x": .5, "y": .12},
            background_normal="",
            background_color=(0, .25, .05, 1),
            color=VERDE
        )
        self.botao.bind(on_press=self.alternar)
        self.rootbox.add_widget(self.botao)

        for _ in range(35):
            coluna = Label(
                text=self.caracteres(),
                color=VERDE,
                font_size=random.randint(12, 22),
                size_hint=(None, None),
                size=(25, 35),
                pos=(random.randint(0, 350),
                     random.randint(0, 700))
            )
            self.raindrops.append(coluna)
            self.rootbox.add_widget(coluna)

        Clock.schedule_interval(self.animar, 0.08)
        Window.bind(size=self.redimensionar)
        return self.rootbox

    def caracteres(self):
        return random.choice("01アイウエオカキクケコ")

    def redimensionar(self, window, size):
        self.status.text = "SYSTEM ONLINE"

    def alternar(self, instance):
        self.rodando = not self.rodando
        self.botao.text = (
            "PAUSAR MATRIX" if self.rodando
            else "RETOMAR MATRIX"
        )
        self.status.text = (
            "SYSTEM ONLINE" if self.rodando
            else "ANIMACAO PAUSADA"
        )

    def animar(self, dt):
        if not self.rodando:
            return

        largura, altura = Window.size
        for coluna in self.raindrops:
            x, y = coluna.pos
            y -= random.randint(5, 18)

            if y < 0:
                y = altura
                x = random.randint(0, max(0, largura - 25))

            coluna.pos = (x, y)
            coluna.text = self.caracteres()

    def on_stop(self):
        Clock.unschedule(self.animar)

if __name__ == "__main__":
    MatrixApp().run()
 Cyberlab-Matrix
