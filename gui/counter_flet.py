import flet as ft
from six import text_type


def main(page : ft.Page):
    page.window.width = 420
    page.window.height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    valore = 0

    def handler_minus(e):
        # print("-")
        v = int(myText.value)
        v = v-1
        myText.value = v
        myText.update()

    def handler_plus(e):
        # print("+")
        v = int(myText.value)
        v = v+1
        myText.value = v
        myText.update()



    myBtnMinus = ft.IconButton(icon = ft.Icons.REMOVE,
                               icon_size = 20,
                               on_click = handler_minus,)
    myBtnPlus = ft.IconButton(icon = ft.Icons.ADD,
                              icon_size=20,
                              on_click = handler_plus,)
    myText = ft.TextField(value = 0,
                          width = 100,
                          disabled = True,
                          text_size = 20,
                          text_align = ft.TextAlign.CENTER,
                          )

    myRow = ft.Row([myBtnMinus, myText, myBtnPlus],
                   alignment = ft.MainAxisAlignment.CENTER,)

    """
    page.controls.append(myBtnMinus)
    page.controls.append(myText)
    page.controls.append(myBtnPlus)
    """
    page.controls.append(myRow)

    page.update()

ft.run(main)