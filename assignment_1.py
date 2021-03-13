# -*- coding: utf-8 -*-
"""Assignment_1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AnqMFAis5OR4ddhCwrOLkBEsEelR_y2i
"""

import random as rd
 
sample_data = 100000
 
list_of_balls_bag1 = [0,0,0,0,1,1,1]
red_count_bag1 = black_count_bag1 = 0 
# 0 corresponds to black ball
# 1 corresponds to red ball
 
for i in range(sample_data):
  temp = rd.randint(0, 6)
  if(list_of_balls_bag1[temp] == 0):
    black_count_bag1 += 1
  else:
    red_count_bag1 += 1
  
prob_red_bag1 = red_count_bag1 / sample_data
prob_black_bag1 = black_count_bag1 / sample_data
 
list_of_balls_bag2 = [0,0,0,0,0,1,1,1,1]
# 0 corresponds to black ball
# 1 corresponds to red ball
 
#case1: black ball is transferred from bag 1 to bag 2
new1_list_of_balls_bag2 = [0,0,0,0,0,0,1,1,1,1]
# 0 corresponds to black ball
# 1 corresponds to red ball
new1_red_count_bag2 = new1_black_count_bag2 = 0 
 
for i in range(sample_data):
  temp = rd.randint(0, 9)
  if(new1_list_of_balls_bag2[temp] == 0):
    new1_black_count_bag2 += 1
  else:
    new1_red_count_bag2 += 1
 
#probability of red ball being drawn from bag2 after transferring black ball from bag1 to bag2
prob_picking_red_1 = new1_red_count_bag2/sample_data
 
#case2: red ball is transferred from bag 1 to bag 2
new2_list_of_balls_bag2 = [0,0,0,0,0,1,1,1,1,1]
# 0 corresponds to black ball
# 1 corresponds to red ball
new2_red_count_bag2 = new2_black_count_bag2 = 0 
 
for i in range(sample_data):
  temp = rd.randint(0, 9)
  if(new2_list_of_balls_bag2[temp] == 0):
    new2_black_count_bag2 += 1
  else:
    new2_red_count_bag2 += 1
 
#probability of red ball being drawn from bag2 after transferring red ball from bag1 to bag2
prob_picking_red_2 = new2_red_count_bag2/sample_data
 
final_result = (prob_black_bag1*prob_picking_red_1)/(prob_black_bag1*prob_picking_red_1+prob_red_bag1*prob_picking_red_2)
print("Probability that black ball is transferred from bag 1 to bag 2 if red ball is drawn from bag 2 is:{}".format(final_result))