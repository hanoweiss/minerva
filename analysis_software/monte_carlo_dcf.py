from utils_functions import *
import random
import matplotlib.pyplot as plt
from valuation_analysis import *
import statistics as st


#model inputs:
#FCF
#numofshares
#growthrate(ROIC*retention rate)
#shorttermyears
#discountrate
#perpgrowthrate

def generate_gr_and_dr(gr_range, dr_rate):
    """
    :param gr_range: a dictionary which represents a range for growth rate and the expected distribution,
    :param dr_rate: a tuple which represents a range for discount rate,
    :return: the randomized growth rate and discount rate
    """
    gr = generate_number_by_dictionary_dist(gr_range)
    dr = random.randint(dr_rate[0], dr_rate[1])
    return gr, dr


num_simulations = 1000
fig = plt.figure()
plt.title("DCF simulation")
plt.xlabel("iterations")
plt.ylabel("DCF result")
plt.xlim([0, num_simulations])


def run_dcf_simulation(num_simulations):
    num_iterations = []
    dcf_results = []
    ticker = 'ULTA'
    stock_data = get_data_from_api(ticker)
    num_of_years = 5  # for average free cash flow
    short_term_years = 10
    long_term_years = 10
    lt_growth = 0
    perpetuity_growth_rate = 0.02
    margin_of_safety = 0.5
    gr_dict = {(0, 3): 10,
               (4, 8): 70,
               (8, 10): 20}
    dr_tuple = (7, 9)
    fcf = get_avg_free_cash_flow(stock_data, num_of_years)
    num_of_shares = get_number_of_shares(stock_data)
    for i in range(num_simulations):
        num_iterations.append(i)
        gr, dr = generate_gr_and_dr(gr_dict, dr_tuple)
        st_growth = gr/100
        dr_rate = dr/100
        result = calculate_intrinsic_value(fcf, num_of_shares, st_growth, lt_growth, dr_rate, short_term_years,
                                           long_term_years, perpetuity_growth_rate, margin_of_safety)
        dcf_results.append(result[1])

    plt.plot(num_iterations, dcf_results, 's')
    plt.savefig(ticker)
    avg = average(dcf_results)
    median = st.median(dcf_results)
    minimum = min(dcf_results)
    print('Average:', avg, 'Median:', median, 'Min:', minimum)

run_dcf_simulation(1000)


