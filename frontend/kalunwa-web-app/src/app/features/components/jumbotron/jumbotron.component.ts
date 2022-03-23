import { Component, OnInit } from '@angular/core';
import { MatCarousel, MatCarouselComponent } from '@ngmodule/material-carousel';
import { JumbotronModel } from '../../models/slides-model';
import { HomepageService } from '../../service/homepage.service';


@Component({
  selector: 'app-jumbotron',
  templateUrl: './jumbotron.component.html',
  styleUrls: ['./jumbotron.component.scss']
})
export class JumbotronComponent implements OnInit {

  public slides: JumbotronModel[]=[];

  constructor(private homeService: HomepageService) {
  }


  ngOnInit(): void {
    this.homeService.getJumbotron()
      .subscribe(data => this.slides = data);
  }
}
