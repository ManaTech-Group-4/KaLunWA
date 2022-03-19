import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-about-page',
  templateUrl: './about-page.component.html',
  styleUrls: ['./about-page.component.scss']
})
export class AboutPageComponent implements OnInit {

  constructor() { }

  public members: number = 189;
  ngOnInit(): void {
  }

  white = "#00000";
  slides = [{'image': 'assets/images/people/BoT/BoT-1.jpg'},
            {'image': 'assets/images/people/BoT/BoT-2.jpg'},
            {'image': 'assets/images/people/BoT/BoT-3.jpg'},
            {'image': 'assets/images/people/BoT/BoT-4.jpg'},
            {'image': 'assets/images/people/BoT/BoT-5.jpg'},
            {'image': 'assets/images/people/BoT/BoT-6.jpg'},
            {'image': 'assets/images/people/BoT/BoT-7.jpg'},
            {'image': 'assets/images/people/BoT/BoT-8.jpg'},
            {'image': 'assets/images/people/BoT/BoT-9.jpg'},
            {'image': 'assets/images/people/BoT/BoT-10.jpg'},
            {'image': 'assets/images/people/BoT/BoT-11.jpg'},
            {'image': 'assets/images/people/BoT/BoT-12.jpg'},
            {'image': 'assets/images/people/BoT/BoT-13.jpg'},
            {'image': 'assets/images/people/BoT/BoT-14.jpg'},
            {'image': 'assets/images/people/BoT/BoT-15.jpg'}];
}
