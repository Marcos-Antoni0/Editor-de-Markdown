import flet as ft


def main(page: ft.Page):
    page.padding=0
    page.title = 'Markdown Editor'
    def update_view(e):
        view.value = editor.value
        view.update()

    editor = ft.TextField(
        multiline=True, # Ativar várias linhas
        min_lines=25, # Minimo de linhas
        max_lines=30, # Máximo de linhas
        color=ft.colors.BLACK,
        content_padding=ft.padding.all(30), # Espaçamento entre as bordas
        border=ft.InputBorder.NONE, #Deixar sem borda
        bgcolor=ft.colors.BLUE_GREY,
        on_change=update_view

    )
    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
          scroll=ft.ScrollMode.ALWAYS,
          controls=[
              ft.Text(value='Para criar titulos em diferentes tamanhos', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
              ft.Text(value='# H1', color=ft.colors.GREY_700),
              ft.Text(value='## H2', color=ft.colors.GREY_700),
              ft.Text(value='### H3', color=ft.colors.GREY_700),
              ft.Divider(color=ft.colors.GREY, height=40),

              ft.Text(value='Para formatar o estilo do texto', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
              ft.Text(value='**Texto em negrito**', color=ft.colors.GREY_700),
              ft.Text(value='*Texto em italico*', color=ft.colors.GREY_700),
              ft.Text(value='~~Texto tachado~~', color=ft.colors.GREY_700),
              ft.Divider(color=ft.colors.GREY, height=40),

              ft.Text(value='Para criar listas', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
              ft.Text(value='1. Ordenada', color=ft.colors.GREY_700),
              ft.Text(value='- Não ordernada', color=ft.colors.GREY_700),
              ft.Divider(color=ft.colors.GREY, height=40),

              ft.Text(value='Inserir links e imagens', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
              ft.Text(value='[Texto do link](https://www.cloudflare.com/pt-br/)', color=ft.colors.GREY_700),
              ft.Text(value='![Label da image](image.jpg)', color=ft.colors.GREY_700),
              ft.Divider(color=ft.colors.GREY, height=40),

              ft.Text(value='Inserir código', weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
              ft.Text(value='`print("Código em uma linha")`', color=ft.colors.GREY_700),
              ft.Text(value='```\nprint("Código em multiplas linhas") \n```', color=ft.colors.GREY_700),
              ft.Divider(color=ft.colors.GREY, height=40),                        
            
          ]
        )
    )

    view = ft.Markdown(
        value=editor.value,
        selectable=True, # Permitir selecionar o conteúdo fo Markdown
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB, # Formato de markdown
        code_theme='monokai-sublime', # Tema bloco de código
        on_tap_link=lambda e: page.launch_url(e.data), # Redirecionar quando clicar em link
        )

    layout = ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to
                    ]
                )

            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(30),
                content=view

            ),
        ]
    )
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)