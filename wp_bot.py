from flask import Flask, request
import sqlite3
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def search_book(book_name):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE LOWER(TITLE) LIKE LOWER(?)", ('%' + book_name + '%',))
    record = cursor.fetchone()

    conn.close()
    return record


@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()

    book = search_book(incoming_msg)

    resp = MessagingResponse()

    if book:
        quantity, title, author, price = book

        reply = f"""📚 Book Found!

Title: {title}
Author: {author}
Price: ₹{int(price)}
Stock: {int(quantity)}
"""
    else:
        reply = "❌ Book not available"

    resp.message(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)