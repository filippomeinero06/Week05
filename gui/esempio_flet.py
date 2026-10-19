import asyncio

import flet as ft

async def main(page : ft.Page):
    myText = ft.Text("Il mio testo", size = 24, color = "blue")
    page.controls.append(myText) # Aggiungo alla lista dei controlli della pagina l'etichetta di testo

    for i in range(1,100):
        myText.value = f"{i}"

        await asyncio.sleep(1) # Aspetta 1 sec
        myText.update()







    page.update() # Aggiorno la pagina

# main() non si chiama così
ft.run(main) # si fa così