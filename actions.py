from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import wikipedia
import nba_py
import timeit
import nba_api

from rasa_core_sdk.events import UserUtteranceReverted
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

class ActionQueryWikipedia(Action):
    def name(self):
        return "action_query_wikipedia"

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.current_state()['latest_message']['text']

        try:
            wiki_summary = wikipedia.summary(last_message)
            dispatcher.utter_message(wiki_summary)
        except:
            dispatcher.utter_message('I was not able to find any information on "{}!" Did you misspell a player\'s name?'.format(last_message))
            return []

class ActionGetEastStandings(Action):
    def name(self):
        return "action_get_east_standings"

    def run(self, dispatcher, tracker, domain):
        from nba_api.stats.endpoints import leaguestandings

        try:
            league_standings = leaguestandings.LeagueStandings().get_normalized_json()
            dispatcher.utter_message(league_standings)
        except Exception as e:
            dispatcher.utter_message('Request took too long to complete. Passing an exception: {}'.format(e))
            pass

        return []

class ActionGetWestStandings(Action):
    def name(self):
        return "action_get_west_standings"

    def run(self, dispatcher, tracker, domain):
        from nba_api.stats.endpoints import leaguestandings

        try:
            league_standings = leaguestandings.LeagueStandings().standings.get_json()
            dispatcher.utter_message(league_standings)
        except Exception as e:
            dispatcher.utter_message('Request took too long to complete. Passing an exception: {}'.format(e))
            pass

        return []

class ActionGetLeagueLeaders(Action):
    def name(self):
        return "action_get_league_leaders"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('getting league leader stats is current a stub.')
        return []

class ActionGetTeamNextGame(Action):
    def name(self):
        return "action_get_team_next_game"

    # def find_team_id(tracker):
    #     last_message = tracker.current_state()['latest_message']['text']
    #     team_id = ''
    #
    #     with open('/data/teams.json') as f:
    #         data_read = json.load(f)
    #
    #     for item in data_read:
    #         if item['teamName'] in last_message or item['location'] in last_message \
    #             team_id = item['teamId']
    #
    #     return team_id

    # def get_games(team_abv):
    #     from nba_api.stats.endpoints import leaguegamefinder
    #
    #     team_id = find_team_id(tracker)
    #     game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)
    #
    #
    #
    #     return team_id

    def run(self, dispatcher, tracker, domain):
        from nba_api.stats.statics import teams

        # try:
        #     get_games()
        # except Exception as e:
        #     dispatcher.utter_message('Failed to gather a teams games. Error: {}'.format(e))

        return []

class ActionGetTeamCoach(Action):
    def name(self):
        return "action_get_teams_coach"

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.current_state()['latest_message']['text']

        dispatcher.utter_message(last_message)

        return []
