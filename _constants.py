daily_death_prob = 0.01
daily_cured_prob = 0.01
mu_r = 1 - pow(1 - daily_cured_prob, 1 / 24)
mu_d = 1 - pow(1 - daily_cured_prob, 1 / 24)
beta_I = 1.96/24/100 #0.06
beta_E = 0.01*beta_I
initial_I = 30 # num of initial I
total_city_pop = 5.6 * 1e6 # singapore
global_contact_num = 10/24 #every day 10 person
theta_l = 1e-3
theta_g = global_contact_num/total_city_pop
gamma = 1/(24*4)# 4 days