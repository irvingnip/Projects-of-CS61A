test = {
  'name': 'Problem 9',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '51af82f6e288537985ce1676eb78d0cc',
          'choices': [
            r"""
            It is watersafe, so its armor won't be reduced to 0 when it is
            placed in a Water Place
            """,
            r"""
            It is not watersafe, so its armor will be reduced to 0 when it is
            placed in a Water Place
            """,
            'It throws water pellets instead of leaves'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How is a ScubaThrower different from a regular ThrowerAnt?'
        },
        {
          'answer': 'ecfbb3193a1d9676a49d194888245675',
          'choices': [
            'name, is_watersafe, food_cost',
            'food_cost, action, damage',
            'is_watersafe, action',
            'name, nearest_bee, is_watersafe'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which inherited attributes and/or methods should ScubaThrower
          override?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing ScubaThrower parameters
          >>> scuba = ScubaThrower()
          >>> ScubaThrower.food_cost
          50ae32be3e31df6c59633df7fdfb3a72
          # locked
          >>> scuba.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing if ScubaThrower is watersafe
          >>> water = Water('Water')
          >>> ant = ScubaThrower()
          >>> water.add_insect(ant)
          >>> ant.place is water
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> ant.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing that ThrowerAnt is not watersafe
          >>> water = Water('Water')
          >>> ant = ThrowerAnt()
          >>> water.add_insect(ant)
          >>> ant.place is water
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> ant.armor
          73b94a1326ae2e803c3421016112207b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing ScubaThrower on land
          >>> place1 = gamestate.places["tunnel_0_0"]
          >>> place2 = gamestate.places["tunnel_0_4"]
          >>> ant = ScubaThrower()
          >>> bee = Bee(3)
          >>> place1.add_insect(ant)
          >>> place2.add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.armor  # ScubaThrower can throw on land
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing ScubaThrower in the water
          >>> water = Water("water")
          >>> water.entrance = gamestate.places["tunnel_0_1"]
          >>> target = gamestate.places["tunnel_0_4"]
          >>> ant = ScubaThrower()
          >>> bee = Bee(3)
          >>> water.add_insect(ant)
          >>> target.add_insect(bee)
          >>> ant.action(gamestate)
          >>> bee.armor  # ScubaThrower can throw in water
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing ScubaThrower Inheritance from ThrowerAnt
          >>> def new_action(self, gamestate):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> ThrowerAnt.action = new_action
          >>> test_scuba = ScubaThrower()
          >>> try:
          ...     test_scuba.action(gamestate)
          ... except NotImplementedError:
          ...     print('inherits action!')
          inherits action!
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_scuba = ScubaThrower()
          >>> try:
          ...     test_scuba.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     print('inherits throw_at!')
          inherits throw_at!
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
      >>> old_thrower_action = ThrowerAnt.action
      >>> old_throw_at = ThrowerAnt.throw_at
      """,
      'teardown': r"""
      >>> ThrowerAnt.action = old_thrower_action
      >>> ThrowerAnt.throw_at = old_throw_at
      """,
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> ScubaThrower.implemented
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
