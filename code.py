        MDButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press:
                root.manager.current = "game"

            MDButtonText:
                text: "PLAY"
                font_size: "80sp"
                theme_text_color: "Custom"
                text_color: "white"

<Ship@Image>:
    source: "assets/images/rocket.png"
    size_hint: None, None
    size: dp(100), dp(300)

<GameScreen>:
    FloatLayout:
        FloatLayout:
            id: game
            FloatLayout:
                id: back
            FloatLayout:
                id: front
                Ship:  
                    id: ship
                    center: root.center       

        FloatLayout:
            id: interface
