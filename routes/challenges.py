from flask import Blueprint, request, jsonify
import os

from openai import OpenAI
model_name = os.getenv('OPENAI_COMPLETION_MODEL')

challenges = Blueprint('challenges', __name__)

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

@challenges.route('/getChallenges', methods=['GET'])
def getChallenges():
    challenges = [
        {
            'id': 1,
            'name': 'Challenge 1',
            'description': 'This is a challenge!',
            'date': 1714929114,
            'images': [
                {
                    'id': 1,
                    'url': 'https://via.placeholder.com/150'
                },
                {
                    'id': 2,
                    'url': 'https://via.placeholder.com/150'
                }
            ]
        },
        {
            'id': 2,
            'name': 'Challenge 2',
            'description': 'This is a challenge!',
            'date': 1714929113,
            'images': [
                {
                    'id': 1,
                    'url': 'https://via.placeholder.com/150'
                },
                {
                    'id': 2,
                    'url': 'https://via.placeholder.com/150'
                }
            ]
        },
        {
            'id': 3,
            'name': 'Challenge 3',
            'description': 'This is a challenge!',
            'date': 1714929112,
            'images': [
                {
                    'id': 1,
                    'url': 'https://via.placeholder.com/150'
                },
                {
                    'id': 2,
                    'url': 'https://via.placeholder.com/150'
                }
            ]
        },
        {
            'id': 4,
            'name': 'Challenge 4',
            'description': 'This is a challenge!',
            'date': 1714929111,
            'images': [
                {
                    'id': 1,
                    'url': 'https://via.placeholder.com/150'
                },
                {
                    'id': 2,
                    'url': 'https://via.placeholder.com/150'
                }
            ]
        },
        {
            'id': 5,
            'name': 'Challenge 5',
            'description': 'This is a challenge!',
            'date': 1714929110,
            'images': [
                {
                    'id': 1,
                    'url': 'https://via.placeholder.com/150'
                },
                {
                    'id': 2,
                    'url': 'https://via.placeholder.com/150'
                }
            ]
        }
    ]
    return jsonify(challenges)

@challenges.route('/generateChallenge', methods=['GET'])
def generateChallenge():
    prompt = f"""
    Generate a cooking challenge for a cooking show. 
    Make sure the first sentence is the name of the challenge.
    The rest should be the description of the challenge.
    Make the description very detailed so that the contestants know exactly what they need to do.

    It's OK to come up with a specific recipe, or a more abstract concept for the challenge.

    The following are just examples. Don't copy these examples exactly. Just use them as inspiration.

    Example 1:
    Pizza Fusion Extravaganza. In this challenge, you'll embark on a culinary journey where the beloved pizza meets unexpected cultural influences. Your task is to create a pizza masterpiece by fusing the flavors and ingredients of two distinct cuisines. Whether it's the rich and spicy flavors of Mexican cuisine, the aromatic herbs and spices of Indian cuisine, or the delicate balance of Japanese flavors, the possibilities are endless.

    Your challenge is to carefully select ingredients and cooking techniques from both cuisines to craft a pizza that seamlessly blends the best of both worlds. Will you experiment with a tandoori chicken pizza topped with mango salsa and cilantro yogurt sauce? Or perhaps a sushi-inspired pizza featuring thinly sliced sashimi, wasabi aioli, and pickled ginger? Let your creativity shine as you push the boundaries of traditional pizza-making and create a Pizza Fusion Extravaganza that will leave the judges craving for more.

    Example 2:
    Symphony of Seasons. Create a dessert that celebrates the flavors and ingredients of a specific season, incorporating elements that evoke the essence of that time of year. Your dessert must include at least three components, each highlighting seasonal produce or flavors in a creative and inspired way. For example, if you choose summer, you might feature juicy strawberries in a refreshing sorbet, paired with a basil-infused whipped cream and a delicate lavender shortbread. Pay attention to the balance of flavors and textures, aiming for a harmonious blend that captures the spirit of the season. Additionally, present your dessert with a decorative flair that reflects the colors and mood of your chosen season, inviting diners to savor the taste of summer, autumn, winter, or spring in every bite.

    Example 3:
    Mocha Swirl Cheesecake Bars. These Mocha Swirl Cheesecake Bars are a decadent treat for coffee lovers. Imagine a rich and creamy cheesecake filling swirled with a luscious mocha sauce, all atop a buttery chocolate graham cracker crust. Each bite is a delightful balance of tangy cheesecake and bold coffee flavor, making it the perfect indulgence for any coffee enthusiast. These bars are great for special occasions or as a luxurious afternoon pick-me-up.

    Only respond with the name and description of the challenge. Don't respond with any other context.

    Response:
    """

    chat_completion = client.chat.completions.create(
        messages = [
            {
                'role': 'user',
                'content': prompt
            }
        ],
        model=model_name
    )

    return jsonify(chat_completion.choices[0].message.content)