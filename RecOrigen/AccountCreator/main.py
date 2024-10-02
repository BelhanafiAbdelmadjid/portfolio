if __name__ == "__main__" :
    # website = input("Which website ? ")

    # if website.lower() == "glassdoor":
    # from accounts.glassdoor import glassdoor_signup
    # glassdoor_signup("belhanafi.abdelmadjid@proton.me")

    # from services.email_service import get_account_verification_link,create_account
    # from services.browser_service import BowserBot

    # bowser = BowserBot()
    # create_account(bowser.driver)



    # from protonmail import ProtonMail

    # p = ProtonMail()
    # p.login("belhanafi.abdelmadjid@proton.me","dyjnec-vofpec-nusnI7")


    # ---------------------------------------------------------------------------- #
    # from accounts.glassdoor import GlassDoor

    # g = GlassDoor(proton={"email":"belhanafi.abdelmadjid@proton.me","password":"dyjnec-vofpec-nusnI7"})
    # # g = GlassDoor(proton={"email":"heII0.w0rld@proton.me","password":"dyjnec-vofpec-nusnI7"})
    # g.process()
    # ---------------------------------------------------------------------------- #


    # ---------------------------------------------------------------------------- #
    # from accounts.dice import Dice
    # d = Dice(proton={"email":"belhanafi.abdelmadjid@proton.me","password":"dyjnec-vofpec-nusnI7"},first_name="jisdu",last_name="dev")
    # d.process()
    # ---------------------------------------------------------------------------- #

    # ---------------------------------------------------------------------------- #
    # from accounts.fairygoodboss import Fairygoodboss

    # f = Fairygoodboss(proton={"email":"belhanafi.abdelmadjid@proton.me","password":"dyjnec-vofpec-nusnI7"},first_name="jisdu",last_name="dev")
    # f.process()
    # ---------------------------------------------------------------------------- #

    # ---------------------------------------------------------------------------- #
    # from accounts.drive4southernag import Drive4southernag

    # d = Drive4southernag(proton={"email":"belhanafi.abdelmadjid@proton.me","password":"dyjnec-vofpec-nusnI7"},first_name="jisdu",last_name="dev",phone_number=int(3478217019))
    # d.process()
    # ---------------------------------------------------------------------------- #


    from accounts.virginvoyage import VirginVoyage

    v = VirginVoyage(proton={"email":"belhanafi.abdelmadjid@proton.me","password":"dyjnec-vofpec-nusnI7"},first_name="jisdu",last_name="dev",birth_month="3",birth_day="12",birth_year="2000")
    v.process()

    import time
    time.sleep(50)
    