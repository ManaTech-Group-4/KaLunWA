import { Component, ElementRef, ViewChild } from '@angular/core';
import { NavService } from '../../service/nav.service';

@Component({
  selector: 'app-visitor-landing',
  templateUrl: './visitor-landing.component.html',
  styleUrls: ['./visitor-landing.component.scss']
})
export class VisitorLandingComponent {


  @ViewChild('sidenav') sidenav: ElementRef | undefined;

  isAdmin = true;
  constructor(private navService: NavService) { }


  whatWeDo : boolean = false;
  about: boolean = false;
  orgOverview : boolean = false;

  ngAfterViewInit() {
    this.navService.sidenav = this.sidenav;
  }

  onSelect(){
    this.whatWeDo = false;
    this.about = false;
    this.orgOverview = false;
  }

}
