<MainScreen>:
    MDBoxLayout: 
        orientation: "vertical"     
        padding: "50dp" 
        spacing: "30dp"

        MDIconButton:
            icon: "cog"
            pos_hint: {"right": 1, "top": 1}
            icon_size: "50dp"

        MDLabel:
            text: "SHOOTER"
            halign: "center"
            font_size: "60sp"

        Image:
            source: "assets/images/rocket.png"
            size_hint_y: 0.7
            allow_stretch: True


        MDButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_press:
                root.manager.current = "game"

            MDButtonText:
                text: "PLAY"
                font_size: "80sp"


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
