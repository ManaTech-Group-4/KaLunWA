import { Component, ViewChild, ElementRef, ViewEncapsulation, AfterViewInit} from '@angular/core';
import { NavService } from './features/service/nav.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class AppComponent implements AfterViewInit {
  title = 'kalunwa-web-app';
  @ViewChild('sidenav') sidenav: ElementRef | undefined;


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
