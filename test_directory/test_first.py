from playwright.sync_api import Page, expect


def test_wiki(page: Page):
    page.goto('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
    page.get_by_role('link', name='свободную энциклопедию').click()
    expect(page.get_by_text('Свобо́дный конте́нт, свобо́дная информа́ция, также свобо́дное содержи́мое/содержа́ние или свобо́дные материа́лы')).to_be_visible()

def test_wiki2(page: Page):
    page.goto('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
    page.get_by_role('link', name='свободную энциклопедию').click()  # нашел элемент, кликнул
    page.get_by_role('link', name='Заглавная страница').click() # нашел элемент по роли и названию, кликнул
    page.locator('#ca-talk').click()  # нашел элемент по css локатору, кликнул
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение:Заглавная страница') # ожидаю что в элементе, найденному по css-локатору, будет оттображаться текст
