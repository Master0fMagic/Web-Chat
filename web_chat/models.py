from flask_login import UserMixin

from datetime import datetime
from web_chat import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.INTEGER, primary_key=True)
    nickname = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    register_time=db.Column(db.Float, nullable=False)


    def __repr__(self):
        return f'<user : {self.nickname}; register time: {datetime.fromtimestamp(self.register_time).strftime("%d.%m.%Y at %H:%M:%S")}>'

    def get_contacts(self):
        '''Return list of all users nicknames'''
        try:
            contacts=User.query.all()
            contacts= [contact.nickname for contact in contacts ]
            contacts.remove(self.nickname)
            return contacts
        except:
            return []

class Message(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    text=db.Column(db.Text, nullable= False)
    sent_time=db.Column(db.Float, nullable=False)
    from_nick=db.Column(db.String(50), db.ForeignKey('user.nickname'), nullable= False)
    to_nick = db.Column(db.String(50), db.ForeignKey('user.nickname'), nullable=False)


    def __repr__(self):
        return  f'<From user {self.from_nick} to user {self.to_nick} at {datetime.fromtimestamp(self.sent_time).strftime("%d.%m.%Y at %H:%M:%S")}: {self.text}>'

    def to_string(self):
        '''Return massage in string format'''
        return f'{self.from_nick} to {self.to_nick} {datetime.fromtimestamp(self.sent_time).strftime("%d.%m.%Y at %H:%M:%S")}: {self.text}'

    @staticmethod
    def get_messages(nickname1, nickname2):
        '''Return list of Messages, that 2 users have'''
        messages = []
        try:
            messages+=Message.query.filter_by(from_nick=nickname1, to_nick=nickname2).all()
            messages+=Message.query.filter_by(from_nick=nickname2, to_nick=nickname1).all()
            flag=True
            while flag:
                flag=False
                for i in range(len(messages)-1):
                    if messages[i].sent_time > messages[i+1].sent_time:
                        messages[i],messages[i+1]=messages[i+1],messages[i]
                        flag=True
        finally:
            return messages

    @staticmethod
    def get_new_messages(nickname1, nickname2, last_message_time):
        ''' Return list of new Messages, that 2 users have'''
        messages = []
        try:
            messages+=Message.query.filter_by(from_nick=nickname1, to_nick=nickname2 ).all()
            messages+=Message.query.filter_by( from_nick=nickname2, to_nick=nickname1).all()
            flag=True
            while flag:
                flag=False
                for i in range(len(messages)):
                    if messages[i].sent_time <= float(last_message_time):
                        messages.remove(messages[i])
                        flag = True
                        break
                for i in range(len(messages)-1):
                    if messages[i].sent_time > messages[i+1].sent_time:
                        messages[i],messages[i+1]=messages[i+1],messages[i]
                        flag=True
        finally:
            return messages



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)