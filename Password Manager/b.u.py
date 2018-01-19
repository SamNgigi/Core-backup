def tearDown(self):
      """
      This tearDown function cleans up after every test case.

      For example in this case...what we want is to return our password_list
      array to default even after multiple saves.
      """
      Passwords.password_list = []

      def test_save_profile(self):
            """
            Test Case to test if the contact object is saved.

            So here it seems like we save try save our profile using a function on
            p_manager that we  have not built.
            This is what causes our test to fail and will only work when we build
            it and then import the working one
            """
            self.new_profile.save_profile()
            self.assertEqual(len(Passwords.password_list), 1)

        def test_save_multiple_profiles(self):
            """
            Test to see if our function can save multiple contacts.
            """
            test_profile = Passwords("Twitter", "newtwitteruser", "14")
            """
            test_profile does not need "self". Its a local variable
            """
            test_profile.save_profile()
            self.new_profile.save_profile()
            self.assertEqual(len(Passwords.password_list), 2)

        def test_delete_profile(self):

def save_profile(self):
    """
    Here we build our save profile function that will append every account
    and password profile.
    When we import it and use it on our test_save profile test-case...it
    should work.
    """
    Passwords.password_list.append(self)
