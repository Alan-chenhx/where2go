// https://vuex.vuejs.org/en/state.html

export default {
  authStatus: '',
  currUserId: null,
  currPlanId: null,
  userProfile: {},
  plans: {},
  itinerary: [
    [
      {
        city: "Los Angeles",
        duration: "120",
        name: "Santa Monica Museum of Art",
        rating: 2.8,
        timetonext: 3.0
      },
      {
        city: "Los Angeles",
        duration: "120",
        name: "Fantastic Race",
        rating: 4.8,
        timetonext: 5.0
      },
      {
        city: "Los Angeles",
        duration: "120",
        name: "Chinatown",
        rating: 1.4,
        timetonext: 0
      }
    ],
    [
      {
        duration: "60",
        name: "Griffith Observatory",
        rating: 4.6,
        timetonext: 0.0
      },
      {
        duration: "30",
        name: "Rebel Without a Cause Monument",
        rating: 1.0,
        timetonext: 6.0
      },
      {
        duration: "150",
        name: "Los Angeles Zoo & Botanical Gardens",
        rating: 2.7,
        timetonext: 11.0
      },
      {
        duration: "90",
        name: "Guinness World Records Museum",
        rating: 1.9,
        timetonext: 0
      }
    ],
    [
      {
        duration: "240",
        name: "Museum of Tolerance",
        rating: 4.2,
        timetonext: 6.0
      },
      {
        duration: "30",
        name: "Diorama-museum of Bhagavad-gita",
        rating: 4.9,
        timetonext: 3.0
      },
      {
        duration: "90",
        name: "The Wende Museum of the Cold War",
        rating: 4.8,
        timetonext: 0
      }
    ],
    [
      {
        duration: "60",
        name: "Santa Monica Pier",
        rating: 4.1,
        timetonext: 61.0
      },
      {
        duration: "120",
        name: "The Huntington Desert Garden",
        rating: 5.0,
        timetonext: 63.0
      },
      {
        duration: "300",
        name: "Universal Studios Hollywood",
        rating: 4.4,
        timetonext: 0
      }
    ],
    [
      {
        duration: "240",
        name: "Studio Tour",
        rating: 4.7,
        timetonext: 100.0
      },
      {
        duration: "330",
        name: "Disneyland Park",
        rating: 4.2,
        timetonext: 0
      }
    ],
    [
      {
        duration: "300",
        name: "Luigi's Rollickin' Roadsters",
        rating: 4.2,
        timetonext: 0
      }
    ],
    [
      {
        city: "San Diego",
        duration: "360",
        name: "LEGOLAND California",
        rating: 2.7,
        timetonext: 0
      }
    ],
    [
      {
        duration: "300",
        name: "SeaWorld San Diego",
        rating: 4.1,
        timetonext: 0
      }
    ],
    [
      {
        duration: "180",
        name: "USS Midway Museum",
        rating: 4.8,
        timetonext: 6.0
      },
      {
        duration: "90",
        name: "AxeVentures",
        rating: 4.9,
        timetonext: 77.0
      },
      {
        duration: "300",
        name: "San Diego Zoo",
        rating: 4.5,
        timetonext: 0
      }
    ]
  ]
}
