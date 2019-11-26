from survivor_league import league, schedule_generator


NUM_PLAYERS = 50
NUM_SIMULATIONS = 1000


def run_simulation():
    strategy_victory_outcome_dict = dict()
    strategy_victory_dict = dict()
    strategy_elimination_week_dict = dict()
    strategy_end_result_dict = dict()
    strategy_cumulative_elimination_probability = dict()
    strategy_average_winnings_dict = dict()
    num_weeks = 0
    num_winners = 0

    for strategy in league.STRATEGIES:
        strategy_name = strategy().name
        strategy_victory_outcome_dict[strategy_name] = 0
        strategy_victory_dict[strategy_name] = 0
        strategy_elimination_week_dict[strategy_name] = dict()
        strategy_end_result_dict[strategy_name] = dict()
        strategy_average_winnings_dict[strategy_name] = 0

    for _ in range(NUM_SIMULATIONS):
        schedule = schedule_generator.ScheduleGenerator().generate_schedule()
        lg = league.League(NUM_PLAYERS, schedule)
        lg.simulate_season()
        results = lg.PLAYERS
        was_tie = len([result for result in results if result.is_alive()]) == 0

        simulation_weeks = 0
        for result in results:
            if result.elimination_week() is None:
                continue
            simulation_weeks = max(simulation_weeks, result.elimination_week())
        num_weeks += simulation_weeks

        simulation_winners = [result for result in results if
                              result.is_alive() or (was_tie and result.elimination_week() == simulation_weeks)]
        num_winners += len(simulation_winners)

        for winner in simulation_winners:
            strategy_victory_dict[winner.strategy_name()] += 1 / len(simulation_winners)
            strategy_victory_outcome_dict[winner.strategy_name()] += 1 / (len(results) - len(simulation_winners) + 1)
            strategy_average_winnings_dict[winner.strategy_name()] += 1

        strategy_player_count = dict()
        for result in results:
            if result.strategy_name() not in strategy_player_count:
                strategy_player_count[result.strategy_name()] = 0
            strategy_player_count[result.strategy_name()] += 1
        strategy_loser_count = dict()
        for result in results:
            if result.is_alive() or (was_tie and result.elimination_week() == simulation_weeks):
                continue
            if result.strategy_name() not in strategy_loser_count:
                strategy_loser_count[result.strategy_name()] = 0
            strategy_loser_count[result.strategy_name()] += 1
        for result in results:
            if result.is_alive() or (was_tie and result.elimination_week() == simulation_weeks):
                continue
            if result.elimination_week() not in strategy_elimination_week_dict[result.strategy_name()]:
                for week in range(result.elimination_week()):
                    if week not in strategy_elimination_week_dict[result.strategy_name()]:
                        strategy_elimination_week_dict[result.strategy_name()][week] = 0
                        strategy_end_result_dict[result.strategy_name()][week] = 0
                strategy_elimination_week_dict[result.strategy_name()][result.elimination_week()] = 0
                strategy_end_result_dict[result.strategy_name()][result.elimination_week()] = 0
            strategy_elimination_week_dict[result.strategy_name()][result.elimination_week()] += \
                1 / strategy_loser_count[result.strategy_name()]
            strategy_end_result_dict[result.strategy_name()][result.elimination_week()] += \
                1 / strategy_player_count[result.strategy_name()]

    for k in strategy_victory_dict.keys():
        strategy_victory_dict[k] /= NUM_SIMULATIONS
    for k in strategy_victory_outcome_dict.keys():
        strategy_victory_outcome_dict[k] /= NUM_SIMULATIONS
    for s in strategy_elimination_week_dict.keys():
        for w in strategy_elimination_week_dict[s]:
            strategy_elimination_week_dict[s][w] /= NUM_SIMULATIONS
    for s in strategy_end_result_dict.keys():
        if s not in strategy_cumulative_elimination_probability:
            strategy_cumulative_elimination_probability[s] = {0: 0}
        for w in strategy_end_result_dict[s]:
            strategy_end_result_dict[s][w] /= NUM_SIMULATIONS
            strategy_cumulative_elimination_probability[s][w] = 0
            for wn in range(w):
                strategy_cumulative_elimination_probability[s][w] += strategy_end_result_dict[s][wn]
            strategy_cumulative_elimination_probability[s][w] += strategy_end_result_dict[s][w]
    for s in league.STRATEGIES:
        strategy_name = s().name
        strategy_average_winnings_dict[strategy_name] = strategy_victory_dict[strategy_name] / \
            strategy_average_winnings_dict[strategy_name] * NUM_SIMULATIONS

    print("Average maximum simulation week number:")
    print(num_weeks / NUM_SIMULATIONS)
    print("Average number of winners:")
    print(num_winners / NUM_SIMULATIONS)
    print("Odds a strategy wins:")
    print(strategy_victory_dict)
    print("Odds of winning, by strategy:")
    print(strategy_victory_outcome_dict)
    print("Odds of being eliminated in a week, by strategy")
    for strategy, elimination_odds in strategy_end_result_dict.items():
        print(strategy, elimination_odds)
    print("Elimination week distribution, by strategy:")
    for strategy, elimination_odds in strategy_elimination_week_dict.items():
        print(strategy, elimination_odds)
    print("Cumulative elimination probability, by strategy")
    for strategy, elimination_odds in strategy_cumulative_elimination_probability.items():
        print(strategy, elimination_odds)
    print("Average player winnings, by strategy")
    for strategy, average_winnings in strategy_average_winnings_dict.items():
        print(strategy, average_winnings)


if __name__ == "__main__":
    run_simulation()
