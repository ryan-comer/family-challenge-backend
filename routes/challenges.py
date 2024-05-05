from flask import Blueprint, request, jsonify

challenges = Blueprint('challenges', __name__)

@challenges.route('/getChallenges', methods=['GET'])
def getChallenges():
    challenges = [
        {
            'id': 1,
            'name': 'Challenge 1',
            'description': 'This is a challenge!',
            'date': 1714929114
        },
        {
            'id': 2,
            'name': 'Challenge 2',
            'description': 'This is a challenge!',
            'date': 1714929113
        },
        {
            'id': 3,
            'name': 'Challenge 3',
            'description': 'This is a challenge!',
            'date': 1714929112
        },
        {
            'id': 4,
            'name': 'Challenge 4',
            'description': 'This is a challenge!',
            'date': 1714929111
        },
        {
            'id': 5,
            'name': 'Challenge 5',
            'description': 'This is a challenge!',
            'date': 1714929110
        }
    ]
    return jsonify(challenges)