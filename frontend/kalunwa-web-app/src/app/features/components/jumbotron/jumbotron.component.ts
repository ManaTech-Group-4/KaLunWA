import { Component, OnInit } from '@angular/core';
import { MatCarousel, MatCarouselComponent } from '@ngmodule/material-carousel';


@Component({
  selector: 'app-jumbotron',
  templateUrl: './jumbotron.component.html',
  styleUrls: ['./jumbotron.component.scss']
})
export class JumbotronComponent implements OnInit {

  constructor() {
  }

  ngOnInit(): void {
  }
  white = "#00000";
  slides = [{'image': 'assets/images/carousel/carousel4.jpg'},
            {'image': 'assets/images/carousel/carousel3.jpg'},
            {'image': 'assets/images/carousel/carousel2.jpg'},
            {'image': 'assets/images/carousel/carousel1.jpg'}];


}
