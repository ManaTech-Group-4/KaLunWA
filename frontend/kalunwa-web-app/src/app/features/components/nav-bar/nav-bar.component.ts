import { Component, OnInit } from '@angular/core';
import { NavService } from '../../service/nav.service';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.scss']
})
export class NavBarComponent implements OnInit {

  constructor(public navService : NavService) { }
  whatWeDo : boolean = false
  about: boolean = false;
  orgOverview : boolean = false;


  ngOnInit(): void {
  }

}
