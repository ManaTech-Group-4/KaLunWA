import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit {

  constructor() { }
  whatWeDo : boolean = false
  about: boolean = false;
  orgOverview : boolean = false;
  ngOnInit(): void {
  }

}
