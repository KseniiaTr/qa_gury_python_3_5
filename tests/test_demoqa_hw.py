from selene.support.shared import browser
from selene import be, have, command
from selene import command


def test_demoqa_hw(size_browser):
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.all(
        '[id^=google_ad][id$=__container__').should(have.size_greater_than_or_equal(3)).perform(command.js.remove)


    browser.element('[id="firstName"]').type('Alex').press_enter()
    browser.element('[id="lastName"]').type('Alekseev').press_enter()
    browser.element('[id="userEmail"]').type('alexalekseev@gmail.com').press_enter()

    browser.element('.custom-control-label').should(have.exact_text('Male')).click()
    browser.element('[id="userNumber"]').type('89101231212')

    browser.element('[id="dateOfBirthInput"]').perform(command.js.set_value('12/02/1990'))
    browser.element('[id="subjectsInput"]').type('History').press_enter()
    browser.element('[for=hobbies-checkbox-3]').click()

    browser.element('[id="uploadPicture"]').send_keys('/Users/caseymac/Desktop/Photo_test_yellow.png')


    browser.element('[id="currentAddress"]').type('Moscow, Pyatnitskaya st 12/12').press_enter()

    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('Delhi').press_enter()


    browser.element('[id="submit"]').press_enter()










