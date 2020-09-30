# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.jsonform -t test_bestellung.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.jsonform.testing.EDI_JSONFORM_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/jsonform/tests/robot/test_bestellung.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Bestellung
  Given a logged-in site administrator
    and an add Bestellung form
   When I type 'My Bestellung' into the title field
    and I submit the form
   Then a Bestellung with the title 'My Bestellung' has been created

Scenario: As a site administrator I can view a Bestellung
  Given a logged-in site administrator
    and a Bestellung 'My Bestellung'
   When I go to the Bestellung view
   Then I can see the Bestellung title 'My Bestellung'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Bestellung form
  Go To  ${PLONE_URL}/++add++Bestellung

a Bestellung 'My Bestellung'
  Create content  type=Bestellung  id=my-bestellung  title=My Bestellung

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Bestellung view
  Go To  ${PLONE_URL}/my-bestellung
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Bestellung with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Bestellung title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
