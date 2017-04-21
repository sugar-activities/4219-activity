from gettext import gettext as _

print _('in texts.py')

upgrade_text_house = [_("Houses would be upgraded to brick and mortar from the mud and thatched roof houses.") , _("Every house would be provided with an outhouse toilet."), _("Electricity connection have been provided to every house.")]
upgrade_text_hospital = [_("Hospitals have been upgraded to brick and mortar from the mud and thatched roof Hospitals."),_("The Hospitals have been renovated and stuffed with investigatory equipments."),_("Hospitals have been provided electricity connection and have been provided with corrugated roof.")]
upgrade_text_school = [_("Schools have been upgraded to brick and mortar from the mud and thatched roof school."),_("School's capacity for number of children who can be educated in the school has increased with upgradation of furniture."),_("Schools have been provided with electricity")]
upgrade_text_workshop = [_("Workshops have been upgraded to brick and mortar from the mud and thatched roof Workshop."),_("Installation of chimney's and mechanised tools have been done."),_("Workshops would be provided outhouse for workers to rest and also have been electrified.")]
upgrade_text_farm = [_("The farms are going to be upgraded so that they would be increasing the production."),_("The villagers are going to be taught about multiple crop farming so that they can grow many crops in the same farm."),_("The villagers are going to be taught about how to use fertilizers for the farms to increase their productivity.")]
upgrade_text_well = [_("Upgrading a well increases the production of water"), _("Upgrading a well increases the production of water"), _("Upgrading a well increases the production of water")]

upgrade_text = {'HOUSE':upgrade_text_house , 'HOSPITAL':upgrade_text_hospital , 'WORKSHOP':upgrade_text_workshop, 'SCHOOL':upgrade_text_school, 'FOUNTAIN': upgrade_text_well, 'FARM':upgrade_text_farm}

trailer_text = [_("Poverty is hunger")+' \n\n'+_("Hunger is Poverty  ")+'\n\n'+_("WFP and SEETA aim to break this vicious cycle"),
                _("When disaster strikes")+' \n\n'+_("WFP brings food to the hungry")+' \n\n'+_("SEETA brings spirit and knowledge to fightback"),
                _("Aim : Manage crisis, rebuild lives and bring back peace, ")+'\n\n'+_("prosperity and sustainability"),
                _("Join the Food Force "),
                _("Help your people become Physically, Socially, ")+'\n\n'+_("Mentally AND Spiritually healthy  "),
                _("Grow food")+' \n\n'+_("Trade food")+' \n\n'+_("Make your village Self-sufficient")+' \n\n'+_("Give your community a balanced diet"),
                _("You decide  ")+'\n\n'+_("What to Grow?")+' \n\n'+_("What to Sell?  ")+'\n\n'+_("What to Buy?  ")+'\n\n'+_("Where to Invest? "),
                _("Wise decisions for a sustainable growth ")+'\n\n'+_("Breaking the vicious cycle of hunger and poverty")]




instruction_text = [_("Welcome to Gokul village. \nJoin the Food Force and make your community healthy and village self-sufficient. \n\nYou can \n-Grow food.\n-Buy food.\n-Trade goods.\n-Help meet the basic necessities of your community: \n  food, \n  water \n  and shelter. \n-Invest in health and education. "),
                    _("Living  \n\nHouse \nOne house per family- Help build housing for safe, secure and healthy living. \n\nSanitation \nHelp upgrade to an outhouse toilet per house. \n\nFarm \nSetup farms and help provide balanced diet to your community. \n\nWell \nWater is the key to survival and sustainence.\nUpgrade your well to get more water."),
                    _("Community \n\nWorkshop \nBuild materials and tools for construction of facilities. \n\nSchool \nInvest in education, invest in growth. Build schools. Use indicators to measure performance. \n\nHospital \nBuild hospitals for prevention and cure of diseases, provide vaccination to infants \nand organize events for community hygiene."),
                    _("Resources \n\n Food \n Water \n Medicine \n Books \n Tools \n Construction Materials "),
                    _("Food \n\nProvide balanced diet to your people for a healthy, active and strong community.\nAt Gokul, you grow, buy and eat \n\nRice \nRice is the staple food and major source of carbohydrates at Gokul. \n\nFruit & Vegetables \nSource of vitamins and minerals. About a third of every villager's diet at Gokul is composed of fruits and vegetables. \nGrow them in farm, consume, and trade them (in kilograms) at the market."),
                    _("Beans \nSource of proteins at Gokul. Grow them in farms, consume and trade them (in kilograms) at the market. \n\nSugar, Salt and Oils \nThey are added to your food items. Buy them at the market for your family. \nSugar and oil help you provide carbohydrates and fats. Salt provides you minerals. \nKeep their quantities balanced."),
                    _("Water \nWater is the key to survival and sustainence. \nUsed for drinking, washing and raising crops. \nMaintain and improve the wells for a constant supply of clean water. \n\nMedicine \nMedicine for treatment and cure of diseases. \n\nVaccination for children \nEnsure a steady supply of medicines for a safe and a healthy Gokul."),
                    _("Books \nBooks are meant for young and old, keep them well my friend, their weight is gold. \nMaintain the existing books in school libraries, and order more whenever required. Books on nutrition, hygiene and agriculture will help the community to adapt best practices at Gokul. \n\nTools \nMake or buy tools for maintaining fields and growing crops, and for \nconstruction of facilities. \n\nBuilding Materials \nStraw, wood, mud and bricks compose the building materials. \nProduce building materials at the workshop, or buy them at the market for construction of facilities. ")]

'''




instruction_text = [" Welcome to Gokul!\n This is your village;\n It is up to you to make it grow, thrive and develop.\n\n Some things are produced in the fields and workshops of your village;\n others can be bought at the market.\n\n You need to produce enough to cover the basic needs of your villagers - \n Food, Shelter, Water \n And then you can trade surplus at the market.\n In order to help your village grow and survive,\n\n You also need to invest in health and education.",
                              "FACILITIES\n\n House\n Everyone needs somewhere to live.\n Invest in housing to make the people of Gokul more comfortable\n and safe from disease. Upgrades like an outhouse toilet\n will increase the health indicators of the village considerably!\n\n Farm\n It's vital to keep your farms strong so that people have enough food\n from different food groups to eat a balanced diet.\n\n Well\n Water is key to cultivate your fields and for hygiene and construction!\n Upgrade your well to get more water.",
                              "FACILITIES\n\n Workshop\n This is where you produce tools and building materials\n that will help you construct better facilities for your village.\n\n School\n The better your school, the higher your Education indicator!\n As your population grows, you'll need to invest in schools\n to make sure everyone gets an education.\n\n Hospital\n Make sure you have a health infrastructure in place in your village,\n so that people have somewhere to go when they're ill.\n Hospitals produce medicine, too.",
                              "RESOURCES\n\n These are your resources:\n Food\n Water\n Medicine\n Books\n Tools\n Building Materials\n\n All of them play an important part in building your village. Manage them wisely!\n\n FOOD\n A strong community depends on strong, healthy people\n and nobody can be strong without adequate food,\n Make sure you produce a balanced supply of food\n so that the people of Gokul can be strong and active.\n ",
                              "RESOURCES\n\n Rice\n This is your 'Main Food' - It's important to make sure the people of Gokul\n get enough to eat, and it's what they will eat the most of.\n But you need 'helper' foods to make the people of Gokul healthy and strong.\n\n Fruit & Vegetables\n About a third of people's diet should be made up of fruit and vegetables\n to give them all the vitamins and minerals they need to be strong.\n Grow fruit and vegetable in the fields of Gokul\n or buy and trade them at the market.\n\n Beans\n Protein - either in the form of legumes, groundnuts or meat, poultry or eggs - \n is an important food to help us grow strong.\n Grow beans in the fields of Gokul or buy and trade them at the market.\n ",
                              "RESOURCES\n\n Sugar\n Salt\n Oils\n\n These are all important energy helpers to make people active and strong,\n but should only be a small part of the diet compared to the main food.\n Buy these goods at the Gokul market.\n",
                              "RESOURCES\n\n Water\n Without water, there is no life. \n You'll need it for people to drink and wash,\n but also to build things in the village and to water your crops.\n Maintain and improve the village wells\n to make sure you have a constant supply of clean water.\n\n Medicine\n Malaria, AIDS, pneumonia..\n Make sure your village always has enough medicine to treat people\n from the threats that come up. The stronger people are through better\n nutrition and education, the less medicine you'll need.\n Buy medicines at the market;\n you need to make sure your hospitals get a steady supply.\n",
                              "RESOURCES\n\n Books\n There's nothing in this world that someone hasn't written a book about!\n You'll need plenty of books to educate the people of Gokul\n about important issues like nutrition, hygiene, and lots of other things.\n Books can only be bought at the market;\n you need to have a supply of them to run a school.\n\n Tools\n You'll need tools to till your fields and make the\n materials to build houses and other buildings.\n Produce them at the workshops or buy them at the market.\n\n Building Materials\n Straw, wood, bricks.. build, improve and maintain the constructions of Gokul\n with these essential materials.\n Produce them at the workshops or buy them at the market."
                              ]
'''

about_us_text = _('Living is learning. Learning is living.')+' \n\n'+_('We define learning as a compound formed by three elements: ')+'\n\n'+_('Education - learning from ones physical, social and spiritual environment')+' \n'+_('Training - how to learn learning')+' \n'+_('Entertainment - learning should always be fun, Happy Learning')+' \n\n'+_('Our vision is to engineer and deploy interactive platforms to enable and cherish learning.')+' \n\n'+_('Please write to us at discuss@seeta.in for opinions, feedback and ideas for ')+'\n'+_('development. ')+'\n\n'+_('We look forward to hearing from you.')
