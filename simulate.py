from survivor_league import league, schedule_generator


NUM_SIMULATIONS = 10


def run_simulation():
    strategy_victory_dict = dict()
    strategy_elimination_week_dict = dict()
    num_weeks = 0
    num_winners = 0

    for strategy in league.STRATEGIES:
        strategy_name = strategy().name
        strategy_victory_dict[strategy_name] = 0
        strategy_elimination_week_dict[strategy_name] = dict()

    for _ in range(NUM_SIMULATIONS):
        schedule = schedule_generator.ScheduleGenerator().generate_schedule()
        lg = league.League(schedule)
        lg.simulate_season()
        results = lg.PLAYERS
        was_tie = len([result for result in results if result.is_alive()]) == 0

        results_dict = dict()
        for result in results:
            results_dict[result.name()] = {
                'strategy': result.strategy_name(),
                'elimination_week': result.elimination_week()
            }

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

        strategy_week_count = dict()
        for result in results:
            if result.is_alive() or (was_tie and result.elimination_week() == simulation_weeks):
                continue
            if result.strategy_name() not in strategy_week_count:
                strategy_week_count[result.strategy_name()] = 0
            strategy_week_count[result.strategy_name()] += 1
        for result in results:
            if result.is_alive() or (was_tie and result.elimination_week() == simulation_weeks):
                continue
            if result.elimination_week() not in strategy_elimination_week_dict[result.strategy_name()]:
                for week in range(result.elimination_week()):
                    if week not in strategy_elimination_week_dict[result.strategy_name()]:
                        strategy_elimination_week_dict[result.strategy_name()][week] = 0
                strategy_elimination_week_dict[result.strategy_name()][result.elimination_week()] = 0
            strategy_elimination_week_dict[result.strategy_name()][result.elimination_week()] += \
                1 / strategy_week_count[result.strategy_name()]

    for k in strategy_victory_dict.keys():
        strategy_victory_dict[k] /= NUM_SIMULATIONS
    for s in strategy_elimination_week_dict.keys():
        for w in strategy_elimination_week_dict[s]:
            strategy_elimination_week_dict[s][w] /= NUM_SIMULATIONS

    print("Average maximum simulation week number:")
    print(num_weeks / NUM_SIMULATIONS)
    print("Average number of winners:")
    print(num_winners / NUM_SIMULATIONS)
    print("Odds of winning, by strategy:")
    print(strategy_victory_dict)
    print("Odds of being eliminated each week, by strategy:")
    for strategy, elimination_odds in strategy_elimination_week_dict.items():
        print(strategy, elimination_odds)


if __name__ == "__main__":
    run_simulation()
