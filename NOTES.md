Armadillo
=========

DataModel:

Sponsor
  Name          String
  Description   String
  Logo          URL
  
Meetup
  DateTime      DateTime
  Location      String
  Sponsors      [Sponsor]
  MeetupRSVPs   Integer
  TotalVotes    Integer
  TotalPizzas   Integer

Pizza
  Name          String
  Description   Sting
  Ingredients   [String]
  Vegetarian    Boolean
  
  ImageURL      URL
  VoteCount     Integer
  OrderCount    Integer

User
  email         String
  VoteCount     Integer
  Vegeterian    Boolean




