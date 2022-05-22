import { Component, OnInit } from '@angular/core';
import { EventsModel } from './../../models/events';
import { HomepageService } from './../../service/homepage.service';
import { HomeCampModel } from './../../models/home-camp';
import { HomeNewsModel } from './../../models/home-news';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.scss']
})
export class HomepageComponent implements OnInit {


  constructor(private homeService: HomepageService) { }


  whatWeDo : boolean = false
  about: boolean = false;
  orgOverview : boolean = false;

  public events = [] as EventsModel[];
  public projects = [] as EventsModel[];
  public news =[] as HomeNewsModel[];
  public camps : HomeCampModel[] = [
    {
      title:"Baybayon",
      img: "assets/images/baybayon.png",
      color: "#ECDBB2"
    },
    {
      title:"Lasang",
      img: "assets/images/lasang.png",
      color: "#3F6218"
    },
    {
      title:"Suba",
      img: "assets/images/suba.png",
      color: "#1C8BD4"
    },
    {
      title:"Zero Waste",
      img: "assets/images/zero.png",
      color: "#9CCC65"
    },
  ];

  ngOnInit(): void {
    this.homeService.getEvents()
      .subscribe(data => this.events = data);

    this.homeService.getProjects()
      .subscribe(data => this.projects = data);

    this.homeService.getNews()
    .subscribe(data => this.news = data);
  }


}
