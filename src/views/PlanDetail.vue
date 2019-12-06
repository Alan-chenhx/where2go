<template>
  <v-content>
    <v-container>
      <v-row>
        <v-col cols="1" :v-if="!loading">
          <div>
            <div class="d-flex flex-column" style="height: 90vh;overflow-y: auto;position: fixed;">
              <div
                class="text-center"
              >{{ toDate(0).toLocaleString('default', { month: 'short' }).toUpperCase()}}</div>
              <div v-for="n in numDays" :key="n">
                <div
                  class="text-center"
                  v-if="toDate(n-1).getMonth() != toDate(n-2).getMonth()"
                >{{ toDate(n-1).toLocaleString('default', { month: 'short' }).toUpperCase() }}</div>
                <v-btn
                  class="black--text ma-0"
                  @click="scrollToDate(n-1)"
                  icon
                  text
                >{{ toDate(n-1).getDate() }}</v-btn>
              </div>
            </div>
          </div>
        </v-col>
        <v-col cols="8" :v-if="!loading">
          <v-timeline dense>
            <div v-for="(day, i) in itinerary" :key="i">
              <v-timeline-item fill-dot small :id="'date-'+i">
                <template v-slot:icon>
                  <v-sheet
                    class="title text-no-wrap pa-2 white--text"
                    color="black"
                  >{{toDate(i).toLocaleString('default', { weekday: 'short', day: 'numeric', month: 'short'})}}</v-sheet>
                </template>
              </v-timeline-item>
              <v-timeline-item
                large
                class="align-center"
                v-if="!!day[0].city?(i>0&&!!itinerary[i-1][0].city)?day[0].city!=itinerary[i-1][0].city:true:false"
              >
                <span class="headline text-center text-no-wrap">{{day[0].city}}</span>
              </v-timeline-item>
              <draggable :v-model="day" :group="'city'+day[0].city">
                <div v-for="(attr, j) in day" :key="j">
                  <v-timeline-item>
                    <template v-slot:icon>
                      <v-sheet
                        class="text-no-wrap pa-2 white--text text-center"
                        color="purple"
                        min-width="90"
                      >{{attr.duration}} mins</v-sheet>
                    </template>
                    <v-card class="elevation-3">
                      <v-img
                        gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
                        :src="attr.photo"
                        max-height="150"
                        class="white--text v-card--reveal;"
                      >
                        <v-card-title class="headline" :class="attr.photo?'white--text':'black--text'">
                          {{ attr.name }}
                          <v-btn
                            rounded
                            class="ml-5"
                            @click="deleteAttr(currPlanId, attr.city, attr.name, i, j)"
                          >
                            <v-icon>clear</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-card-subtitle :class="attr.photo?'white--text':'black--text'">{{ attr.address }}</v-card-subtitle>
                        <v-row align="center" class="mx-0">
                          <v-rating
                            class="ml-4"
                            :value="attr.rating"
                            color="amber"
                            dense
                            half-increments
                            readonly
                            size="14"
                            v-if="!!attr.rating"
                          ></v-rating>
                          <div :class="attr.photo?'white--text ml-4':'black--text ml-4'" v-if="!!attr.rating">{{attr.rating}}</div>
                          <div :class="attr.photo?'white--text ml-4':'black--text ml-4'">{{ attr.tag }}</div>
                        </v-row>
                      </v-img>
                      <v-card-text>
                        <div
                          style="display: -webkit-box;-webkit-line-clamp: 5; -webkit-box-orient: vertical;overflow: hidden;"
                        >{{ attr.description }}</div>
                      </v-card-text>
                    </v-card>
                  </v-timeline-item>
                  <v-timeline-item
                    class="align-center"
                    color="white"
                    fill-dot
                    v-if="attr.timetonext!=0"
                  >
                    <template v-slot:icon>
                      <v-icon color="black">mdi-car</v-icon>
                    </template>
                    <span>{{ attr.timetonext }} mins</span>
                  </v-timeline-item>
                </div>
              </draggable>
            </div>
          </v-timeline>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script>
import draggable from "vuedraggable";
import { mapState, mapActions } from "vuex";

Date.prototype.addDays = function(day) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + day);
  return date;
};

export default {
  name: "PlanDetail",
  components: {
    draggable
  },
  data: () => ({
    itinerary: [
      [
        {
          duration: "90",
          address: "700 Jean St, Oakland, CA 94610-1459",
          rating: 4.7,
          name: "Morcom Amphitheater of Roses",
          photo: "",
          description:
            "Morcom Amphitheater of Roses is located in Oakland. Make Morcom Amphitheater of Roses a part of your Oakland vacation plans using our Oakland trip itinerary planner .",
          tag: ["Garden"],
          url:
            "https://www.inspirock.com/united-states/oakland/morcom-amphitheater-of-roses-a4272781519",
          timetonext: 3,
          city: "Oakland"
        },
        {
          duration: "120",
          address: "666 Bellevue Ave, Oakland, CA 94610, USA",
          rating: 4.4,
          name: "Lakeside Park and Garden Center",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/lakeside-park-and-garden-center-656608282.jpg",
          description:
            "Lakeside Park located in Oakland, California is a retirement community that offers Memory Care on a comfortable senior campus notable for its positive, safe, residential environment as well as the best in memory care services. Lakeside Park\u2019s charming location is near scenic Lake Merritt and the popular Lakeside Park with close access to shopping, dining, entertainment and healthcare in Berkeley and all points in the East Bay. Choose from a private studio or shared suite. Meals are centered upon fresh, local and healthy food choices, allowing residents to eat when they are hungry, while still providing a variety of healthy and delicious snacks. Residents of Lakeside Park, a nationally recognized community providing the highest level of care for those with Alzheimer\u2019s, enjoy services and amenities catered specifically to each individual.",
          tag: ["Garden"],
          url:
            "https://www.inspirock.com/united-states/oakland/lakeside-park-and-garden-center-a34457097",
          timetonext: 1.0,
          city: "Oakland"
        },
        {
          duration: "120",
          address: "300 Lakeside Dr, Oakland, CA 94612-3534",
          rating: 4.6,
          name: "Kaiser Center Roof Garden",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/kaiser-center-roof-garden--748900934.jpg",
          description:
            "Kaiser Center, also called the Kaiser Building, is a 28 story office building located at 300 Lakeside Drive, adjacent to Lake Merritt, in downtown Oakland, California, designed by the architectural firm of Welton Becket & Associates of Los Angeles. The property is bounded by Lakeside Drive, which terminates and joins Harrison Street at the site, 20th-, 21st-, and Webster-streets. When completed in 1960, it was Oakland's tallest building, as well as the largest office tower west of the Rocky Mountains. A three-story office/retail building adjacent to the main tower was completed in 1963. Kaiser Center was the headquarters of Kaiser Industries, a Fortune 500 conglomerate that was headed by industrialist Edgar F. Kaiser at the time the building was constructed.The building's roof garden was designed by San Francisco-based landscape architecture firm, Theodore Osmundson & Associates, and was the first built in the United States after World War II. While legend has it that Henry J. Kaiser resided in a penthouse apartment on the 28th floor, by 1960 the elder Kaiser had turned over the Oakland-based company to his son, and pursued projects based in Honolulu. It is much more likely that his son Edgar, who was in charge of Kaiser industries and a major power broker in the Bay Area by the time the building was commissioned, was the person who occupied any residential apartments. According to a National Park Service study, Edgar commissioned the architecturally significant rooftop garden after the building had been designed, inspired by the gardens of Rockefeller Center in N.Y.",
          tag: ["Garden"],
          url:
            "https://www.inspirock.com/united-states/oakland/kaiser-center-roof-garden-a4278119379",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "120",
          address: "2869 Broadway, Oakland, CA 94612, USA",
          rating: 4.5,
          name: "Cat Town Cafe",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/cat-town-cafe--1876500381.jpg",
          description:
            "Cat Town is a non-profit cat rescue dedicated to finding loving homes for Oakland's at-risk shelter cats, by proving them safe, comfortable spaces outside the shelter cage in a foster home or at our adoption center at 2869 Broadway. If you\u2019re planning on visiting us at Cat Town, here is some info to help you and the cats have an enjoyable experience. The Cat Zone:- We have between 10 - 20 free roaming cats who are available for adoption. You can visit with them whether you're adopting or just looking for some quality cat time. Most of our cats come from our local municipal shelter, Oakland Animal Services. When cats are adopted through Cat Town, it means we can get another cat out of a shelter cage and ready to find their new family. - We allow 10 people to enter every hour on the hour. This is to help limit the stress and over stimulation of our four legged friends.- Walk-ins are welcome to enter for a $5 donation fee if there is available space that hour. We highly recommend that you make a Cat Zone reservation online at www.bookeo.com/cattown for a $10 donation fee, especially on weekends. This will ensure your visiting time is available and you'll support a great cause in the process. - You are welcome to bring cafe food and beverage into the Cat Zone, but please don\u2019t bring your own cat!- Volunteers will be on hand to answer any questions you have about cats, adoptions, our organization, and cat related things.General Info:- Cats sleep a lot. They also hide a lot. This is natural and healthy. Our cats meet up to 100 people a day, 5 days a week. If you\u2019re itching for play time, we recommend coming early for the 10AM and 11AM hours, or in the evening for the 6PM hour, when the cats are most active.- We are dedicated to the safety and well-being of our cats. Their comfort and safety is our first priority.- We serve local coffee and pastries in our cafe space. We have limited indoor and outdoor seating, plus viewing windows into the Cat Zone should we reach capacity.- We are closed Mondays & Tuesdays to acclimate new cats to the space and give our current residents some much deserved rest.Thank you for your interest in our organization and the work we do. We would be no where without our supporters. See you at the Cafe soon!",
          tag: ["Entertainment Center"],
          url:
            "https://www.inspirock.com/united-states/oakland/cat-town-cafe-a2280464435",
          timetonext: 4,
          city: "Oakland"
        },
        {
          duration: "120",
          address: "1000 Oak St, Oakland, CA 94607, USA",
          rating: 4.8,
          name: "Oakland Museum of California",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/oakland-museum-of-california--76274379.jpg",
          description:
            "Take a comprehensive tour of the Golden State at Oakland Museum of California. Through more than a million artifacts and three separate galleries, the museum tells the story of California's history, arts, and nature. At the historical gallery, browse artifacts depicting everything from the native communities, Spanish settlers, and Gold Rush, to the rise of Hollywood and the present day. The art gallery displays numerous works of famous Californian artists, while the natural science section celebrates the extensive diversity of the state's wildlife. The museum's many amenities include a cafe, bike and car parking, and free Wi-Fi access. The entire facility is adapted to accommodate visitors with special needs and parents with small children. Use our Oakland tour itinerary maker website  to add Oakland Museum of California and other attractions to your Oakland vacation plans.",
          tag: ["Must See", "Specialty Museum"],
          url:
            "https://www.inspirock.com/united-states/oakland/oakland-museum-of-california-a522927301",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "90",
          address:
            "650 Bellevue Ave, near the Lakeside Garden Center, Oakland, CA 94610-5000",
          rating: 4.6,
          name: "GSBF Bonsai Garden at Lake Merritt",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/gsbf-bonsai-garden-at-lake-merritt--1221678739.jpg",
          description:
            "GSBF Bonsai Garden at Lake Merritt is located in Oakland. Take a look at our Oakland road trip planner to schedule your visit to GSBF Bonsai Garden at Lake Merritt and learn about what else to see and do during your holiday.",
          tag: ["Garden"],
          url:
            "https://www.inspirock.com/united-states/oakland/gsbf-bonsai-garden-at-lake-merritt-a4277952179",
          timetonext: 10.0,
          city: "Oakland"
        },
        {
          duration: "120",
          address: "2777 Middle Harbor Rd, Oakland, CA 94607, USA",
          rating: 4.2,
          name: "Middle Harbor Shoreline Park",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/middle-harbor-shoreline-park-1645581025.jpg",
          description:
            "Middle Harbor Shoreline Park is located on San Francisco Bay and the Port of Oakland entrance channel, west of downtown Oakland, California. It is owned and operated by the Port of Oakland. The park entrance is at the intersection of 7th and Middle Harbor Streets. It is open Monday through Friday, 9 AM to 5 PM, and closed Saturdays and Sundays. The park is primarily on land that was the former site of the Oakland Naval Supply Depot (1940\u22121998), which was an important supply base for the Pacific Fleet of the U. S. Navy throughout World War II. The Naval Supply Depot closed in 1998, and the 541acre facility was transferred to the Port of Oakland, which still owns it.The section adjacent to the Port of Oakland, which includes Port View Park, was originally part of the Oakland Long Wharf or Oakland Pier\u2212Mole, which was the massive western terminus of the Southern Pacific Railroad into San Francisco Bay. The interlocking tower from the railroad's pier has been moved and partially restored as a small commemorative museum. The mast of the is displayed at the entrance of the park.A 38acre area was redeveloped for the park from 2002 to 2004. Redevelopment of the land included restoration of beaches and creation of a lagoon. The park was opened to the public on September 18, 2004.  There is an amphitheater overlooking San Francisco Bay where live entertainment performs. The Chappell R. Hayes Memorial Observation Tower, named to honor the West Oakland leader, offers good views of the Oakland Estuary and the Port's shipping activities. Interpretive signs throughout the park present the history of the site, the environmental resources here and the adjacent maritime activities. A viewing area for observing the super-Panamax cranes in operation at the adjacent Hanjin Terminal.",
          tag: ["Park"],
          url:
            "https://www.inspirock.com/united-states/oakland/middle-harbor-shoreline-park-a1263805653",
          timetonext: 2.0,
          city: "Oakland"
        },
        {
          duration: "30",
          address: "4292 7th St, Oakland, CA, United States",
          rating: 3.8,
          name: "Port View Park",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/port-view-park--19535528.jpg",
          description:
            "Port View Park is located in Oakland. Port View Park is just one of the many highlights you can arrange to see using our online itinerary creator, Oakland Edition.",
          tag: ["Pier / Boardwalk"],
          url:
            "https://www.inspirock.com/united-states/oakland/port-view-park-a8327492247",
          timetonext: 19.0,
          city: "Oakland"
        },
        {
          duration: "90",
          address: "125 I St, Sacramento, CA 95814, USA",
          rating: 4.8,
          name: "California State Railroad Museum",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/california-state-railroad-museum--1035275708.jpg",
          description:
            'Dedicated to the "iron horse" that connected the Golden State to the rest of the country, California State Railroad Museum holds over 20 locomotives and railroad cars. Watch for the large-scale model of the Donner Pass that allowed trains to pass through the Sierra Nevada mountains--it prompts photos from many visitors. Other locomotives outside have been restored to gleaming chrome and dark iron. Book a tour through the railcars, given by costumed train enthusiasts, who explain the mechanics and the lifestyle on the tracks. Put California State Railroad Museum into our Sacramento tour planning website  and find out what\'s close by, where to stay, and where to head next.',
          tag: ["Must See", "Specialty Museum"],
          url:
            "https://www.inspirock.com/united-states/sacramento/california-state-railroad-museum-a73906705",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "120",
          address: "2501 Grizzly Peak Boulevard, Orinda, CA 94563, USA",
          rating: 4.8,
          name: "Tilden Regional Park",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/tilden-regional-park--2078066172.jpg",
          description:
            "Tilden Regional Park is located in Berkeley. Put Tilden Regional Park at the forefront of your travel plans using our Berkeley driving holiday website .",
          tag: ["Park"],
          url:
            "https://www.inspirock.com/united-states/berkeley/tilden-regional-park-a15941833",
          timetonext: 11.0,
          city: "Oakland"
        },
        {
          duration: "150",
          address: "7087 Skyline Blvd, Oakland, CA 94611, USA",
          rating: 4.8,
          name: "Huckleberry Botanic Regional Preserve",
          description:
            'Huckleberry Botanic Regional Preserve is a 241acre regional park and nature reserve in the Berkeley Hills, in the eastern East Bay (San Francisco Bay Area) region of the San Francisco Bay Area of California. It is within Alameda and Contra Costa Counties. It is a park within the East Bay Regional Parks District system. The Preserve is named after the California Huckleberry (Vaccinium ovatum) which grows abundantly within its habitat.GeographyThe Huckleberry Botanic Regional Preserve is on the crest of the Oakland Hills, located above Oakland and Orinda. It represents a relic plant association found only in certain areas along the coastal climate region of California, where specific soil and climatic conditions still exist. It is a very diverse botanical area for native plants of the mixed evergreen forest and montane chaparral and woodlands ecoregions and plant communities. Trails connect the preserve with Robert Sibley Volcanic Preserve on the north, and Redwood Regional Park on the south."Huckleberry Botanic Regional Preserve." Oakland Wiki. Accessed September 1, 2017.',
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/huckleberry-botanic-regional-preserve--912714130.jpg",
          tag: ["Park"],
          url:
            "https://www.inspirock.com/united-states/oakland/huckleberry-botanic-regional-preserve-a1374872813",
          timetonext: 8.0,
          city: "Oakland"
        },
        {
          duration: "120",
          address: "7867 Redwood Rd, Oakland, CA 94619, USA",
          rating: 4.8,
          name: "Redwood Regional Park",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/redwood-regional-park--1737130029.jpg",
          description:
            "The sight drop on the map seems to change, due to the dual nature of Skyline Boulevard (it has the same address at the preserve on Skyline just south of the Joaquin Miller Road intersection, as Roberts Regional Park's 115000 address UP Skyline Boulevard FROM the same intersection. If coming from Joaquin Miller to the south, cross the intersection with the light. It becomes Skyline. make a turn through the island in the middle of the road into the loop shaped parking lot which is visible on the map. If coming up Skyline from the south, simply pull into the lot, which is the only possible right turn BEFORE the intersection mentioned above, where from this direction Skyline BECOMES Joaquin Miller Road. :-D",
          tag: ["Park"],
          url:
            "https://www.inspirock.com/united-states/oakland/redwood-regional-park-a7249725665",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "90",
          address: "3125 St. Helena Hwy, St. Helena, CA 94574-9706",
          rating: 4.9,
          name: "Modus Operandi Cellars",
          photo: "https://s.inspirockcdn.com/images/defaults/wineries.jpg",
          description:
            "Modus Operandi Cellars is located in St. Helena. To visit Modus Operandi Cellars and get the most from your holiday in St. Helena, create itinerary details personal to you using our St. Helena trip planner .",
          tag: ["Must See", "Winery / Vineyard"],
          url:
            "https://www.inspirock.com/united-states/st-helena/modus-operandi-cellars-a1381545233",
          timetonext: 0.0,
          city: "Oakland"
        },
        {
          duration: "360",
          address:
            "29359 Arnold Drive,, Turn 1, Sonoma Raceway, Sonoma, CA, United States",
          rating: 4.6,
          name: "Simraceway Performance Driving Center",
          description:
            "A leading racing school with world-class instructors operating from a state-of-the-art facility at the finest road course in America The Simraceway Performance Driving Center graduates hundreds of career-minded racers and thousands of motoring enthusiasts each year, so whether you\u2019re seeking a life-changing experience or yearning for the experience of a lifetime, take a look at the wide range of programs and courses we offer to find out what we can do for you.",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/simraceway-performance-driving-center-1432869004.jpg",
          tag: ["Must See", "Auto Race Track"],
          url:
            "https://www.inspirock.com/united-states/sonoma/simraceway-performance-driving-center-a192774531",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "120",
          address: "453 1st St E, Sonoma, CA 95476, USA",
          rating: 4.6,
          name: "Sonoma Plaza",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/sonoma-plaza--2911495.jpg",
          description:
            "At the heart of Sonoma Valley, Sonoma Plaza offers historical sightseeing, shopping, dining, and arts. See the early 20th-century city hall that's still in use and the Bear Flag monument that marks the spot of an 1846 Mexican-American War revolt. Browse the shops for clothing, bags, jewelry, and books. Because of its proximity to wine country, you can choose from among an array of wine cellars and tasting rooms and indulge in local and imported brands. You'll find plenty of galleries here that feature historical and contemporary pieces from around the world, and the area offers numerous spots for photography. Start your visit at the visitors' bureau on the east side of the plaza. Use our Sonoma trip itinerary builder website  to add Sonoma Plaza and other attractions to your Sonoma vacation plans.",
          tag: ["Park"],
          url:
            "https://www.inspirock.com/united-states/sonoma/sonoma-plaza-a45962999",
          timetonext: 31.0,
          city: "Oakland"
        },
        {
          duration: "90",
          address: "703 Oakville Crossroad, Oakville, CA 94562",
          rating: 4.8,
          name: "B Cellars Vineyards and Winery",
          photo: "https://s.inspirockcdn.com/images/defaults/wineries.jpg",
          description:
            "B Cellars Vineyards and Winery is located in Oakville. Put B Cellars Vineyards and Winery into our Oakville online tour builder  to see other points of interest to visit during your vacation in Oakville.",
          tag: ["Must See", "Winery / Vineyard"],
          url:
            "https://www.inspirock.com/united-states/oakville/b-cellars-vineyards-and-winery-a3133833417",
          timetonext: 5.0,
          city: "Oakland"
        },
        {
          duration: "150",
          address: "875 Rutherford Rd, Rutherford, CA 94573, USA",
          rating: 4.1,
          name: "Round Pond Estate",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/round-pond-estate--1408678851.jpg",
          description:
            "Round Pond Estate is located in Rutherford. Using our custom trip planner, Rutherford attractions like Round Pond Estate can form part of a personalized travel itinerary.",
          tag: ["Garden"],
          url:
            "https://www.inspirock.com/united-states/rutherford/round-pond-estate-a624712123",
          timetonext: 0,
          city: "Oakland"
        }
      ],
      [
        {
          duration: "90",
          address: "680 Rossi Rd, St Helena, CA 94574, USA",
          rating: 4.8,
          name: "Anderson's Conn Valley Vineyards",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/andersons-conn-valley-vineyards-569070326.jpg",
          description:
            "Anderson's Conn Valley Vineyards represent a hidden gem of Napa Valley, offering an intimate wine tasting experience in a family-owned, traditional-style winery. When you meet the owners and the wine team, you'll receive a personalized and educational journey through a dozen wine samples of lush reds and crisp whites. The tasting can be followed by a short tour of the grounds. Plan to visit Anderson's Conn Valley Vineyards during your St. Helena vacation using our convenient St. Helena day trip site .",
          tag: ["Must See", "Winery / Vineyard"],
          url:
            "https://www.inspirock.com/united-states/st-helena/andersons-conn-valley-vineyards-a1100441031",
          timetonext: 20.0,
          city: "Oakland"
        },
        {
          duration: "90",
          address: "4045 St Helena Hwy, Calistoga, CA 94515, USA",
          rating: 4.1,
          name: "Castello di Amorosa",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/castello-di-amorosa-19051183.jpg",
          description:
            "Sample fine wines and tour a 13th-century Tuscan-style castle at Castello di Amorosa. With a general admission, you explore the first two levels of the castle. Spend extra for the guided tour if you prefer to see more of the grand building. Discover the moat, chapel, drawbridge, and torture chamber, home to a 300-year-old iron maiden torture device. The great hall's frescoes took two Italian artists a year and a half to complete. Climb up one of the defensive towers to take in far-reaching views of the countryside. Once you have finished exploring, descend into tasting rooms to sample wines from the castle's vineyard. To visit Castello di Amorosa on your trip to Calistoga, use our Calistoga trip site .",
          tag: ["Must See", "Castle"],
          url:
            "https://www.inspirock.com/united-states/calistoga/castello-di-amorosa-a724533105",
          timetonext: 7.0,
          city: "Oakland"
        },
        {
          duration: "30",
          address: "3000 Summit Trail, Santa Rosa, CA 95404, USA",
          rating: 4.9,
          name: "Pride Mountain Vineyards",
          photo:
            "https://s.inspirockcdn.com/ds10/photos/United States/1/pride-mountain-vineyards--294429075.jpg",
          description:
            "A strong tradition of Californian winemaking thrives atop Spring Mountain at Pride Mountain Vineyards. These 34 hectares (83 acres) of vineyards straddle the line between Sonoma County and Napa Valley, providing an interesting climate for the grapes and a specific approach to winemaking. This winery has vines dating back to the 19th century, and its winemakers are happy to educate you on the history and process of winemaking. Daily tours include a tasting, tours of the vineyard (weather permitting), and a visit to the winery's caves where around 2,400 barrels are kept. Reservations are required. Use our St. Helena road trip planner to visit Pride Mountain Vineyards on your trip to St. Helena, and learn what else travelers and our writers recommend seeing nearby.",
          tag: ["Must See", "Winery / Vineyard"],
          url:
            "https://www.inspirock.com/united-states/st-helena/pride-mountain-vineyards-a944019049",
          timetonext: 0,
          city: "Oakland"
        }
      ]
    ],
    loading: true,
    input: null,
    nonce: 0
  }),

  computed: {
    ...mapState(["currPlanId", "currStart"]),
    numDays() {
      return this.itinerary.length;
    },
    startDate() {
      return new Date(this.currStart);
    }
  },

  methods: {
    ...mapActions(["fetchPlanDetail", "removeFromItinerary"]),
    log: function(evt) {
      window.console.log(evt);
    },
    async deleteAttr(currPlanId, city, name, i, j) {
      const payload = { planId: currPlanId, city: city, name: name };
      console.log(payload);
      await this.removeFromItinerary(payload).then(
        this.itinerary[i].splice(j, 1)
      );
    },
    toDate(n) {
      return this.startDate.addDays(n + 1);
    },
    scrollToDate(n) {
      this.$vuetify.goTo("#date-" + n);
    },
    comment() {
      const time = new Date().toTimeString();
      this.events.push({
        id: this.nonce++,
        text: this.input,
        time: time.replace(/:\d{2}\sGMT-\d{4}\s\((.*)\)/, (match, contents) => {
          return ` ${contents
            .split(" ")
            .map(v => v.charAt(0))
            .join("")}`;
        })
      });

      this.input = null;
    }
  },

  async created() {
    this.loading = true;
    await this.fetchPlanDetail({ planId: this.currPlanId });
    this.loading = false;
  }
};
</script>