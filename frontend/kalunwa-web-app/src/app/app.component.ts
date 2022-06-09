import { Component, ViewChild, ElementRef, ViewEncapsulation, AfterViewInit, OnInit} from '@angular/core';
import { NavigationEnd, NavigationStart, Router } from '@angular/router';
import { NavService } from './features/service/nav.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class AppComponent implements AfterViewInit, OnInit {
  title = 'kalunwa-web-app';
  @ViewChild('sidenav') sidenav: ElementRef | undefined;

  isAdmin = true;
  constructor(private navService: NavService, private router: Router) { }

  whatWeDo : boolean = false;
  about: boolean = false;
  orgOverview : boolean = false;

  sidebarOpen:boolean=true;

  ngAfterViewInit() {
    this.navService.sidenav = this.sidenav;
    this.router.events.subscribe((evt) => {
        if (!(evt instanceof NavigationEnd)) {
            return;
        }
        window.scrollTo(0, 0)
    });
  }
  ngOnInit(): void {
  }

  onSelect(){
    this.whatWeDo = false;
    this.about = false;
    this.orgOverview = false;
  }

  sidebarToggle(){
    this.sidebarOpen = !this.sidebarOpen;
  }


}
