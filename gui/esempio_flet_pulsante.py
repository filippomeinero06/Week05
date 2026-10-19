import flet as ft

def main(page: ft.Page):
    myText = ft.Text("Hello in red", size = 34, color = "red")

    # Funzione annidata: invocata da Python/Flet quando noi premiamo quel pulsante
    def button_handler():
        myText.color = "green"
        myText.update()
        
    myButton = ft.Button(content="Change color in green", on_click=button_handler)

    page.controls.append(myText)
    page.controls.append(myButton)


    page.update()

ft.run(main)