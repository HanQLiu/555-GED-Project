import unittest
import The_Real_Project03


class TestUS25US27(unittest.TestCase):

    incorrect_ind = {
            '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23],
                     'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA'},
            '@I2@': {'NAME': ['Adam /Levine/', 27], 'SEX': ['F', 21], 'BIRT_DATE': ['1964-02-25', 23],
                     'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA'}
        }
    incorrect_fam = {
            '@F1@': {'HUSB': ['@I10@', 139], 'WIFE': ['@I12@', 140], 'CHIL': [['@I1@', 194], ['@I2@', 195]],
                     'MARR_DATE': ['1995-03-02', 143], 'DIV_DATE': ['1972-03-28', 153]}
        }
    correct_ind = {
            '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23],
                     'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA'},
            '@I2@': {'NAME': ['Suzie /Levine/', 27], 'SEX': ['F', 21], 'BIRT_DATE': ['1974-01-5', 23],
                     'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA'}
        }
    correct_fam = {
            '@F1@': {'HUSB': ['@I10@', 139], 'WIFE': ['@I12@', 140], 'CHIL': [['@I1@', 194], ['@I2@', 195]],
                     'MARR_DATE': ['1995-03-02', 143], 'DIV_DATE': ['1972-03-28', 153]}
        }

    def test_US25(self):
        self.assertFalse(The_Real_Project03.unique_first_name(self.incorrect_ind, self.incorrect_fam))

  
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
