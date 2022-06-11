import { Component, Input, OnInit } from '@angular/core';
import {MatCarouselComponent, MatCarousel } from '@ngmodule/material-carousel';
import { homepageInfo } from '../../models/homepage-container-model';
import { JumbotronModel } from '../../models/slides-model';
import { HomepageService } from '../../service/homepage.service';


@Component({
  selector: 'app-jumbotron',
  templateUrl: './jumbotron.component.html',
  styleUrls: ['./jumbotron.component.scss']
})
export class JumbotronComponent implements OnInit {

  @Input()
  slides: homepageInfo.PageContainedJumbotron[];

  constructor(private homeService: HomepageService) {
  }


  ngOnInit(): void {
  }

}
