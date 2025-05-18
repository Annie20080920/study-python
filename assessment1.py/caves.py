from game import Cave
# new caves
burrow = Cave("burrow", "A deep cave with lots of bugs")
hollow = Cave("hollow", "A small and deep cave under the ground")
 
# link the caves
burrow.link_caves(dungeon, 'north')
burrow.link_caves(hollow, 'east')