import { Component, OnInit } from '@angular/core';
import { AboutCampModel } from '../../models/about-camp-model';

@Component({
  selector: 'app-about-camp',
  templateUrl: './about-camp.component.html',
  styleUrls: ['./about-camp.component.scss']
})
export class AboutCampComponent implements OnInit {

  constructor() { }

  displayCampIndex = 0;
  camps :AboutCampModel[] = [
    {
      id: 1,
    header: "Baybayon",
    featured_img: "assets/images/carousel/carousel1.jpg",
    camp_leader: "Marielle Eliza Mascariñas",
    camp_leader_img: "assets/images/person-icon.jpg",
    short_description:"The term Baybayon translates to Coasts. This camp is the prime unit that seeks to address issues involving our shores. They aim to protect, safeguard, and preserve the purity of coastlines.",
    quote: "You are my fire",
    color: "#D9B863"
    },
    {
      id: 2,
    header: "Lasang",
    featured_img: "assets/images/carousel/carousel2.jpg",
    camp_leader: "Spica Mae Samante",
    camp_leader_img: "assets/images/person-icon.jpg",
    short_description: "The term Lasang translates to Forests. This camp is tasked with upholding the integrity of our forests by any capable means possible. They endeavor to spearhead measures that conserve, manage, and develop our woodlands.",
    quote: "The one desire",
    color: "#3F6218"
    },
    {
      id: 3,
    header: "Suba",
    featured_img: "assets/images/carousel/carousel3.jpg",
    camp_leader: "Noelyn Faith Lopos",
    camp_leader_img: "assets/images/person-icon.jpg",
    short_description: "The term Suba translates to Rivers. This camp  is mandated to pursue campaigns and activities that inoculate freshwater streams. They envision a water resource that meets the needs of its people. ",
    quote: "Believe when I say",
    color: "#1C8BD4"
    },
    {
      id: 4,
    header: "Zero Waste",
    featured_img: "assets/images/carousel/carousel1.jpg",
    camp_leader: "Emirozz Czarlene Labaria",
    camp_leader_img: "assets/images/person-icon.jpg",
    short_description: "The Zero Waste Camp is an ad hoc camp delegated with the unique mission to oversee the Zero Waste Cabilao Island project. They provide undivided attention to the project and focus on its successful completion.",
    quote: "I want it that way",
    color: "#88BB4E"
    }
  ];

  displayCamp: AboutCampModel = this.camps[0];

  ngOnInit(): void {
  }

  onSelect(index:number){
    this.displayCamp = this.camps[index];
  }

}
