import { Component, OnInit } from '@angular/core';
import { AboutCampModel } from '../../models/about-camp-model';
import { AboutpageService } from '../../service/aboutpage.service';

@Component({
  selector: 'app-about-camp',
  templateUrl: './about-camp.component.html',
  styleUrls: ['./about-camp.component.scss']
})
export class AboutCampComponent implements OnInit {

  constructor(private aboutService: AboutpageService) { }

  displayCampIndex = 0;
  camps : AboutCampModel[]=[];
  campLinks = ['lasang', 'zero-waste', 'baybayon', 'suba']
  colors = ["#3F6218","#88BB4E","#D9B863","#1C8BD4"];


  displayCamp: AboutCampModel = this.camps[0];
  ngOnInit(): void {
    this.aboutService.getCampLeaders()
      .subscribe(data => this.camps = data);

    this.displayCamp = this.camps[0];

  }

  onSelect(index:number){
    this.displayCamp = this.camps[index];
  }

}
