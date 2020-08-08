from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, Response
from flask_sqlalchemy import SQLAlchemy
from config import app, db
from model import Person, Account
import sys
import itertools

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/person')
def view():
    person = Person.query.order_by(Person.id).all()

    return render_template('view.html', persons=person)

@app.route('/person', methods=['POST'])
def add():
    try:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        vip = request.form.get('vip')

        person = Person(first_name=first_name, last_name=last_name, vip=bool(vip))

        db.session.add(person)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('view'))

@app.route('/person/<int:person_id>')
def get(person_id):
    person = Person.query.get(person_id)
    account = Account.query.filter_by(person_id=person_id).order_by(Account.balance.desc()).all()
    count = Account.query.filter_by(person_id=person_id).count()
    # print(f'==========> {account}')

    return render_template('get.html', persons=person, accounts=account, counts=count)

@app.route('/person/<int:person_id>/edit')
def edit(person_id):
    person = Person.query.get(person_id)

    return render_template('edit.html', persons=person)

@app.route('/person/<int:person_id>/edit', methods=['POST'])
def modify(person_id):
    try:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        vip = request.form.get('vip')

        person = Person.query.get(person_id)

        person.first_name = first_name
        person.last_name = last_name
        person.vip = bool(vip)

        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('view'))

@app.route('/person/<int:person_id>', methods=['DELETE'])
def delete(person_id):
    try:
        Account.query.filter(Account.person_id==person_id).delete()
        Person.query.filter_by(id=person_id).delete()
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({'success': True})

@app.route('/person/<int:person_id>/create', methods=['POST'])
def create(person_id):
    try:
        get_balance = request.get_json('newBalance')["newBalance"]
        get_person = Person.query.get(person_id)

        new_account = Account(balance=get_balance, person=get_person)

        db.session.add(new_account)
        db.session.commit()
        # print(f'==========> {person_id}')
    except:
        db.session.rollback()
    finally:
        db.session.close()
    
    return jsonify({'success': True})

@app.route('/delete/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    try:
        get_account = Account.query.get(account_id)

        db.session.delete(get_account)
        db.session.commit()
        # print(f'==========> {get_account}')
    except:
        db.session.rollback()
    finally:
        db.session.close()
    
    return jsonify({'success': True})


@app.route('/transaction/<int:account_id>', methods=['POST'])
def transaction(account_id):
    try:
        account = Account.query.get(account_id)
        current_balance = account.balance
        deposit = request.get_json('deposit')["deposit"]
        withdraw = request.get_json('withdraw')["withdraw"]
        new_balance = (int(current_balance) + int(deposit)) - int(withdraw)
        # print(f'==========> ID: {account_id}, Current: {current_balance}, Deposit: {deposit}, Withdraw: {withdraw}, Balance: {new_balance}')

        account.balance = new_balance

        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({'success': True})

@app.route('/account')
def account():
    person = Person.query.join(Account).all()
    item = db.session.query(Person, Account).join(Account).order_by(Person.id).all()
    count = db.session.query(Person, Account).join(Account).order_by(Person.id).count()
    # print(f'=========> {person}')

    return render_template('view_account.html', persons=person, items=item, counts=count)
