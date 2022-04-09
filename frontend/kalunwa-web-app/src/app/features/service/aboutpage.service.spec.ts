import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { AboutCampModel } from '../models/about-camp-model';
import { TotalDemographicsModel } from '../models/demographics-total-model';

import { AboutpageService } from './aboutpage.service';

describe('AboutpageService', () => {
  let service: AboutpageService,
      httpTestingController: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [
        AboutpageService
      ]
    });
    service = TestBed.get(AboutpageService);
    httpTestingController = TestBed.get(HttpTestingController);
  });


  afterEach(()=>{
    httpTestingController.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });


  it('should retrieve total Demographics', () => {
    const testMembers: TotalDemographicsModel =
    {total_members: 100};

    service.getDemographics().subscribe((member)=>{
      expect(testMembers).toBe(member,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/about-us/demographics');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testMembers);

  });


  it('should retrieve all camp info and leaders', () => {
    const testCampLeaders: AboutCampModel[] = [{
          "camp_name": "Suba",
          "description": "default description",
          "camp_image": "http://127.0.0.1:8000/media/images/content/event.jpg",
          "camp_leader": {
              "name": "firstname 1 lastname 1",
              "motto": "",
              "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
          }
      },
      {
          "camp_name": "Baybayon",
          "description": "default description",
          "camp_image": "http://127.0.0.1:8000/media/images/content/event.jpg",
          "camp_leader": {
              "name": "firstname 0 lastname 0",
              "motto": "",
              "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
          }
      },
      {
          "camp_name": "Zero Waste",
          "description": "default description",
          "camp_image": "http://127.0.0.1:8000/media/images/content/event.jpg",
          "camp_leader": {
              "name": "firstname 3 lastname 3",
              "motto": "",
              "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
          }
      },
      {
          "camp_name": "Lasang",
          "description": "default description",
          "camp_image": "http://127.0.0.1:8000/media/images/content/event.jpg",
          "camp_leader": {
              "name": "firstname 2 lastname 2",
              "motto": "",
              "image": "http://127.0.0.1:8000/media/images/content/event.jpg"
          }
      }];

    service.getCampLeaders().subscribe((camps)=>{
      expect(testCampLeaders).toBe(camps,'should check mocked data');
    });

    const req = httpTestingController.expectOne('http://127.0.0.1:8000/api/about-us/camps');

    expect(req.cancelled).toBeFalsy();
    expect(req.request.responseType).toEqual('json');

    req.flush(testCampLeaders);

  });
});
