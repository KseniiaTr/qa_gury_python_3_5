from selene.support.shared import browser
from selene import have
from selene import command
import os


def test_demoqa_hw(size_browser):
    #browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    #browser.all(
        #'[id^=google_ad][id$=__container__').should(have.size_greater_than_or_equal(3)).perform(command.js.remove)

    browser.all('[id^=google_ads][id$=container__]').with_(timeout=5).wait_until(have.size_greater_than_or_equal(3))
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    browser.element('#firstName').type('Alex')
    browser.element('#lastName').type('Alekseev')
    browser.element('#userEmail').type('alexalekseev@gmail.com')

    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('8910123121')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('May')
    browser.element('.react-datepicker__year-select').send_keys('1991')
    browser.element(f'.react-datepicker__day--00{7}').click()


    browser.element('#subjectsInput').type('History').press_enter()
    browser.element('[type=checkbox][id=hobbies-checkbox-3]+label').should(
        have.exact_text('Music')).click()


    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'resources/Photo_test_yellow.png')
        )
    )

    browser.element('#currentAddress').perform(command.js.set_value(
        'Delhi, Pyatnitskaya st 12/12'))
    browser.element('#react-select-3-input').send_keys('NCR').press_enter()
    browser.element('#react-select-4-input').send_keys('Delhi').press_enter()


    browser.element('#submit').perform(command.js.click)


def test_check_info_in_table():
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
                                               'Alex Alekseev', 'alexalekseev@gmail.com', 'Male', '8910123121',
        '07 May,1991', 'History', 'Music', 'Photo_test_yellow.png', 'Delhi, Pyatnitskaya st 12/12', 'NCR Delhi'))
















