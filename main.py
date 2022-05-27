
class User:
    def get_user_with_general_clientid():
        """
        Returns the user who has one client id (object['id']) for prod and qa
        :return user object:
        """
        if is_qa_android():
            user = {
                'ID': '31585119',
                'FirstName': 'Василий',
                'LastName': 'Петечкин',
                'Phone': '79151609623',
                'Email': '31585119@ozon.ru',
                'Password': 'test'
            }
        else:
            user = {
                'ID': '31585119',
                'FirstName': 'Василий',
                'LastName': 'Петечкин',
                'Phone': '79151609623',
                'Email': 'petechkin606@mail.ru'
            }
        return user

    @staticmethod
    def qa_user_without_phone():
        user = {
            "Email": "29430734@ozon.ru",
            "Login": "29430734",
            "FirstName": "Иван",
            "ID": "29430734"
        }
        return user

    def qa_user_with_phone_black_list():
        # пользователь с телефоном в черном списке, есть email
        user = {
            "Email": "177276@ozon.ru",
            "Login": "177276",
            "FirstName": "Иван",
            "ID": "177276",
            "Phone": "79165894921"
        }
        return user
